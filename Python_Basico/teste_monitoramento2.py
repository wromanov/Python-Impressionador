import sys
import os
import time
import datetime
import threading
import subprocess
import platform
import logging
import json
import re
from logging.handlers import RotatingFileHandler
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit,
    QLabel, QMessageBox, QGroupBox, QFileDialog, QScrollArea, QDialog
)
from PyQt5.QtCore import QTimer, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates


# Estilos para os temas
TEMA_CLARO = """
    QWidget {
        background-color: #f0f0f0;
        color: #000000;
    }
    QLineEdit, QListWidget, QGroupBox {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #cccccc;
        padding: 5px;
    }
    QPushButton {
        background-color: #0078d7;
        color: #ffffff;
        border: none;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #005bb5;
    }
    QLabel {
        padding: 5px;
    }
"""

TEMA_ESCURO = """
    QWidget {
        background-color: #2d2d2d;
        color: #ffffff;
    }
    QLineEdit, QListWidget, QGroupBox {
        background-color: #3c3c3c;
        color: #ffffff;
        border: 1px solid #555555;
        padding: 5px;
    }
    QPushButton {
        background-color: #555555;
        color: #ffffff;
        border: none;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #777777;
    }
    QLabel {
        padding: 5px;
    }
"""


# Classe para exibir gráficos de histórico
class GraficoHistorico(QDialog):
    def __init__(self, historico, nome, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Histórico de Uptime/Downtime - {nome}")
        self.setGeometry(100, 100, 800, 600)

        self.historico = historico
        self.nome = nome

        # Cria uma figura do matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # Layout
        layout = QVBoxLayout()

        # Botões para selecionar o período
        botoes_layout = QHBoxLayout()
        self.botao_diario = QPushButton("Diário")
        self.botao_diario.clicked.connect(lambda: self.atualizar_grafico("diario"))
        botoes_layout.addWidget(self.botao_diario)

        self.botao_semanal = QPushButton("Semanal")
        self.botao_semanal.clicked.connect(lambda: self.atualizar_grafico("semanal"))
        botoes_layout.addWidget(self.botao_semanal)

        self.botao_mensal = QPushButton("Mensal")
        self.botao_mensal.clicked.connect(lambda: self.atualizar_grafico("mensal"))
        botoes_layout.addWidget(self.botao_mensal)

        layout.addLayout(botoes_layout)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Plota o gráfico inicial (diário)
        self.atualizar_grafico("diario")

    def filtrar_historico(self, periodo):
        """Filtra o histórico de acordo com o período selecionado."""
        agora = datetime.datetime.now()
        historico_filtrado = []

        for ts, status in self.historico:
            timestamp = datetime.datetime.strptime(ts, "%d-%m-%Y %H:%M:%S")
            if periodo == "diario" and timestamp.date() == agora.date():
                historico_filtrado.append((ts, status))
            elif periodo == "semanal" and timestamp.isocalendar()[1] == agora.isocalendar()[1]:
                historico_filtrado.append((ts, status))
            elif periodo == "mensal" and timestamp.month == agora.month and timestamp.year == agora.year:
                historico_filtrado.append((ts, status))

        return historico_filtrado

    def atualizar_grafico(self, periodo):
        """Atualiza o gráfico com base no período selecionado."""
        historico_filtrado = self.filtrar_historico(periodo)
        timestamps = [datetime.datetime.strptime(ts, "%d-%m-%Y %H:%M:%S") for ts, _ in historico_filtrado]
        status = [1 if s == "ONLINE" else 0 for _, s in historico_filtrado]  # 1 para ONLINE, 0 para OFFLINE

        self.ax.clear()
        self.ax.plot(timestamps, status, marker='o', linestyle='-', color='b')
        self.ax.set_yticks([0, 1])
        self.ax.set_yticklabels(["OFFLINE", "ONLINE"])
        self.ax.set_xlabel("Tempo")
        self.ax.set_ylabel("Status")
        self.ax.set_title(f"Histórico de Uptime/Downtime - {periodo.capitalize()}")
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y %H:%M:%S"))
        self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        self.figure.autofmt_xdate()
        self.canvas.draw()


# Classe para a Tela de Monitoramento
class TelaMonitoramento(QWidget):
    def __init__(self, equipamentos, status_equipamentos, log_file_path):
        super().__init__()
        self.equipamentos = equipamentos
        self.status_equipamentos = status_equipamentos
        self.log_file_path = log_file_path
        self.tema_atual = "claro"  # Tema inicial
        self.setWindowTitle("Monitoramento de Equipamentos")
        self.setGeometry(100, 100, 1000, 600)

        # Layout principal (vertical)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Botão para alternar temas
        self.botao_tema = QPushButton("Alternar Tema (Dark)")
        self.botao_tema.clicked.connect(self.alternar_tema)
        self.layout.addWidget(self.botao_tema)

        # Barra de pesquisa
        self.barra_pesquisa = QLineEdit()
        self.barra_pesquisa.setPlaceholderText("Pesquisar por nome ou IP...")
        self.barra_pesquisa.textChanged.connect(self.filtrar_ativos)  # Filtra em tempo real
        self.layout.addWidget(self.barra_pesquisa)

        # Área de rolagem
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Permite que o conteúdo seja redimensionado
        self.layout.addWidget(self.scroll_area)

        # Widget que contém o conteúdo rolável
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        # Layout para o conteúdo rolável
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Layout para as colunas de online/offline
        self.colunas_layout = QHBoxLayout()
        self.scroll_layout.addLayout(self.colunas_layout)

        # Coluna para ativos online
        self.online_column = QVBoxLayout()
        self.online_column.setAlignment(Qt.AlignTop)
        self.colunas_layout.addLayout(self.online_column)

        # Coluna para ativos offline
        self.offline_column = QVBoxLayout()
        self.offline_column.setAlignment(Qt.AlignTop)
        self.colunas_layout.addLayout(self.offline_column)

        # Títulos das colunas
        online_label = QLabel("Ativos Online")
        online_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.online_column.addWidget(online_label)

        offline_label = QLabel("Ativos Offline")
        offline_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.offline_column.addWidget(offline_label)

        # Dicionário para armazenar os widgets de cada grupo de equipamento
        self.grupos = {}

        # Iniciar atualização da tela
        self.atualizar_tela()

    def alternar_tema(self):
        """Alterna entre os temas claro e escuro."""
        if self.tema_atual == "claro":
            self.tema_atual = "escuro"
            self.botao_tema.setText("Alternar Tema (Claro)")
        else:
            self.tema_atual = "claro"
            self.botao_tema.setText("Alternar Tema (Dark)")
        self.aplicar_tema(self.tema_atual)

    def aplicar_tema(self, tema):
        """Aplica o tema selecionado."""
        if tema == "claro":
            self.setStyleSheet(TEMA_CLARO)
        else:
            self.setStyleSheet(TEMA_ESCURO)

    def filtrar_ativos(self):
        """Filtra os ativos com base no texto da barra de pesquisa."""
        texto_pesquisa = self.barra_pesquisa.text().strip().lower()  # Texto digitado na barra de pesquisa

        for nome, grupo in self.grupos.items():
            ip = self.equipamentos.get(nome, "")
            # Verifica se o nome ou IP contém o texto da pesquisa
            if texto_pesquisa in nome.lower() or texto_pesquisa in ip.lower():
                grupo.show()  # Mostra o grupo se corresponder à pesquisa
            else:
                grupo.hide()  # Oculta o grupo se não corresponder

    def atualizar_tela(self):
        # Limpa as colunas antes de redistribuir os widgets
        self.limpar_colunas()

        # Adiciona os widgets nas colunas corretas
        for nome, ip in self.equipamentos.items():
            if nome not in self.grupos:
                self.criar_grupo_equipamento(nome, ip)

            grupo = self.grupos[nome]
            status_led = grupo.findChild(QLabel)
            last_event_label = grupo.findChild(QLabel, "last_event_label")
            uptime_label = grupo.findChild(QLabel, "uptime_label")
            downtime_label = grupo.findChild(QLabel, "downtime_label")
            ping_label = grupo.findChild(QLabel, "ping_label")
            botao_historico = grupo.findChild(QPushButton, "botao_historico")

            status = self.status_equipamentos.get(nome, {}).get('status', 'OFFLINE')
            status_led.setStyleSheet(
                "background-color: green; width: 20px; height: 20px; border-radius: 10px;"
                if status == "ONLINE"
                else "background-color: red; width: 20px; height: 20px; border-radius: 10px;"
            )

            last_event_time = self.status_equipamentos.get(nome, {}).get('last_event', 'N/A')
            last_event_label.setText(f"Último evento: {last_event_time}")

            uptime = self.calcular_uptime(nome)
            uptime_label.setText(f"Tempo online: {uptime}")

            downtime = self.calcular_downtime(nome)
            downtime_label.setText(f"Tempo offline: {downtime}")

            ping_time = self.status_equipamentos.get(nome, {}).get('ping_time', 'N/A')
            ping_label.setText(f"Ping: {ping_time} ms")

            # Adiciona o grupo na coluna correta
            if status == "ONLINE":
                self.online_column.addWidget(grupo)
            else:
                self.offline_column.addWidget(grupo)

        # Aplica o filtro de pesquisa
        self.filtrar_ativos()

        # Atualiza a tela a cada 5 segundos
        QTimer.singleShot(5000, self.atualizar_tela)

    def limpar_colunas(self):
        # Remove todos os widgets das colunas
        while self.online_column.count():
            item = self.online_column.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        while self.offline_column.count():
            item = self.offline_column.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

    def criar_grupo_equipamento(self, nome, ip):
        # Cria o grupo e retorna ele para ser inserido na grid
        grupo = QGroupBox(f"{nome} ({ip})")
        grupo.setStyleSheet("QGroupBox { font-weight: bold; }")
        grid_sub_layout = QVBoxLayout()

        status_led = QLabel()
        grid_sub_layout.addWidget(status_led)

        last_event_label = QLabel()
        last_event_label.setObjectName("last_event_label")
        grid_sub_layout.addWidget(last_event_label)

        uptime_label = QLabel()
        uptime_label.setObjectName("uptime_label")
        grid_sub_layout.addWidget(uptime_label)

        downtime_label = QLabel()
        downtime_label.setObjectName("downtime_label")
        grid_sub_layout.addWidget(downtime_label)

        ping_label = QLabel()
        ping_label.setObjectName("ping_label")
        grid_sub_layout.addWidget(ping_label)

        botao_historico = QPushButton("Ver Histórico")
        botao_historico.setObjectName("botao_historico")
        botao_historico.clicked.connect(lambda: self.exibir_historico(nome))
        grid_sub_layout.addWidget(botao_historico)

        grupo.setLayout(grid_sub_layout)

        # Armazenar o grupo para não recriar
        self.grupos[nome] = grupo

    def exibir_historico(self, nome):
        """Exibe o gráfico de histórico de uptime/downtime para o equipamento selecionado."""
        historico = self.status_equipamentos.get(nome, {}).get('historico', [])
        if historico:
            dialog = GraficoHistorico(historico, nome, self)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum histórico disponível para este equipamento.")

    def calcular_uptime(self, nome):
        """Calcula o tempo desde que o equipamento foi detectado como ONLINE."""
        if nome in self.status_equipamentos:
            status = self.status_equipamentos[nome].get('status')
            if status == "ONLINE":
                last_online = self.status_equipamentos[nome].get('last_online_time')
                if last_online:
                    tempo_decorrido = datetime.datetime.now() - last_online
                    segundos = int(tempo_decorrido.total_seconds())
                    minutos = segundos // 60
                    horas = minutos // 60
                    dias = horas // 24
                    tempo_formatado = f"{dias} dias, {horas % 24} horas, {minutos % 60} minutos, {segundos % 60} segundos"
                    return tempo_formatado
        return "0 segundos"

    def calcular_downtime(self, nome):
        """Calcula o tempo desde que o equipamento foi detectado como OFFLINE."""
        if nome in self.status_equipamentos:
            status = self.status_equipamentos[nome].get('status')
            if status == "OFFLINE":
                last_offline = self.status_equipamentos[nome].get('last_offline_time')
                if last_offline:
                    tempo_decorrido = datetime.datetime.now() - last_offline
                    segundos = int(tempo_decorrido.total_seconds())
                    minutos = segundos // 60
                    horas = minutos // 60
                    dias = horas // 24
                    tempo_formatado = f"{dias} dias, {horas % 24} horas, {minutos % 60} minutos, {segundos % 60} segundos"
                    return tempo_formatado
        return "0 segundos"


# Classe para a Tela de Administração
class TelaAdministracao(QWidget):
    def __init__(self):
        super().__init__()
        self.equipamentos = {}  # Dicionário para armazenar os equipamentos
        self.status_equipamentos = {}  # Dicionário para armazenar o status dos equipamentos
        self.sistema = platform.system()
        self.comando_ping = "ping -n 1 -w 1000 {}" if self.sistema == "Windows" else "ping -c 1 -W 1 {}"
        self.log_file_path = "log_monitoramento.log"  # Caminho padrão para o arquivo de log
        self.dados_file = "ativos.json"  # Arquivo JSON para persistência
        self.tema_atual = "claro"  # Tema inicial
        self.initUI()
        self.carregar_dados()  # Carrega os dados ao iniciar

    def initUI(self):
        self.setWindowTitle("Administração de Equipamentos")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # Botão para alternar temas
        self.botao_tema = QPushButton("Alternar Tema (Dark)")
        self.botao_tema.clicked.connect(self.alternar_tema)
        layout.addWidget(self.botao_tema)

        self.lista_equipamentos = QListWidget()
        layout.addWidget(self.lista_equipamentos)

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome do Equipamento")
        layout.addWidget(self.nome_input)

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("IP do Equipamento")
        layout.addWidget(self.ip_input)

        self.add_button = QPushButton("Adicionar Equipamento")
        self.add_button.clicked.connect(self.adicionar_equipamento)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover Equipamento")
        self.remove_button.clicked.connect(self.remover_equipamento)
        layout.addWidget(self.remove_button)

        self.monitor_button = QPushButton("Abrir Tela de Monitoramento")
        self.monitor_button.clicked.connect(self.abrir_monitoramento)
        layout.addWidget(self.monitor_button)

        self.salvar_log_button = QPushButton("Escolher local do arquivo de log")
        self.salvar_log_button.clicked.connect(self.escolher_local_log)
        layout.addWidget(self.salvar_log_button)

        self.setLayout(layout)

        # Aplica o tema inicial
        self.aplicar_tema(self.tema_atual)

    def alternar_tema(self):
        """Alterna entre os temas claro e escuro."""
        if self.tema_atual == "claro":
            self.tema_atual = "escuro"
            self.botao_tema.setText("Alternar Tema (Claro)")
        else:
            self.tema_atual = "claro"
            self.botao_tema.setText("Alternar Tema (Dark)")
        self.aplicar_tema(self.tema_atual)

    def aplicar_tema(self, tema):
        """Aplica o tema selecionado."""
        if tema == "claro":
            self.setStyleSheet(TEMA_CLARO)
        else:
            self.setStyleSheet(TEMA_ESCURO)

    def salvar_dados(self):
        """Salva os ativos no arquivo JSON."""
        with open(self.dados_file, "w") as file:
            json.dump(self.equipamentos, file, indent=4)

    def carregar_dados(self):
        """Carrega os ativos do arquivo JSON."""
        if os.path.exists(self.dados_file):
            try:
                with open(self.dados_file, "r") as file:
                    self.equipamentos = json.load(file)
                    # Inicializa o status dos equipamentos
                    for nome in self.equipamentos:
                        self.status_equipamentos[nome] = {
                            'status': "OFFLINE",
                            'last_event': "N/A",
                            'ping_time': "N/A",
                            'historico': []  # Inicializa o histórico
                        }
                    # Atualiza a lista de equipamentos na interface
                    self.lista_equipamentos.clear()
                    for nome, ip in self.equipamentos.items():
                        self.lista_equipamentos.addItem(f"{nome} ({ip})")
                        # Inicia o monitoramento para cada equipamento carregado
                        threading.Thread(target=self.monitorar_equipamento, args=(nome, ip), daemon=True).start()
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Erro", "Arquivo de dados corrompido. Será criado um novo arquivo.")
                self.equipamentos = {}
                self.salvar_dados()

    def escolher_local_log(self):
        caminho_log = QFileDialog.getSaveFileName(self, "Escolha o local para salvar o log", self.log_file_path, "Arquivos de Log (*.log)")
        if caminho_log[0]:
            self.log_file_path = caminho_log[0]
            QMessageBox.information(self, "Sucesso", f"Arquivo de log será salvo em: {self.log_file_path}")

    def validar_ip(self, ip):
        """Valida se o IP está no formato correto."""
        padrao = r"^(\d{1,3}\.){3}\d{1,3}$"
        if re.match(padrao, ip):
            partes = ip.split(".")
            return all(0 <= int(parte) <= 255 for parte in partes)
        return False

    def validar_nome(self, nome):
        """Valida se o nome já está cadastrado."""
        return nome not in self.equipamentos

    def monitorar_equipamento(self, nome, ip):
        """Monitora o status do equipamento em uma thread separada."""
        while nome in self.equipamentos:
            conectado, ping_time = self.verificar_conectividade(ip)
            status_atual = "ONLINE" if conectado else "OFFLINE"

            if self.status_equipamentos.get(nome, {}).get('status') != status_atual:
                if status_atual == "ONLINE":
                    self.status_equipamentos[nome]['last_online_time'] = datetime.datetime.now()
                else:
                    self.status_equipamentos[nome]['last_offline_time'] = datetime.datetime.now()

                self.status_equipamentos[nome]['status'] = status_atual
                self.status_equipamentos[nome]['last_event'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.status_equipamentos[nome]['ping_time'] = ping_time

                # Adiciona o evento ao histórico
                self.status_equipamentos[nome]['historico'].append(
                    (datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), status_atual)
                )

                self.registrar_log(nome, ip, status_atual)

            time.sleep(5)

    def verificar_conectividade(self, ip):
        """Verifica se o equipamento está online usando o comando ping e retorna o tempo de resposta."""
        resultado = subprocess.run(self.comando_ping.format(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if resultado.returncode == 0:
            # Decodifica a saída usando a codificação correta (cp1252 para Windows)
            output = resultado.stdout.decode('cp1252', errors='ignore')
            if self.sistema == "Windows":
                match = re.search(r"tempo[=<](\d+)ms", output)
            else:
                match = re.search(r"time=(\d+\.?\d*) ms", output)
            if match:
                ping_time = match.group(1)
                return True, ping_time
        return False, "N/A"

    def registrar_log(self, nome, ip, status):
        """Registra o status do equipamento no arquivo de log."""
        if not hasattr(self, 'logger'):
            # Cria o diretório de logs se não existir
            if not os.path.exists("logs"):
                os.makedirs("logs")

            # Gera o nome do arquivo de log com a data atual
            data_atual = datetime.datetime.now().strftime("%d_%m_%Y")
            nome_arquivo = f"log_monitoramento_{data_atual}.log"
            caminho_log = os.path.join("logs", nome_arquivo)

            # Configura o logger
            self.logger = logging.getLogger(nome)
            self.logger.setLevel(logging.INFO)

            # Cria um handler para escrever no arquivo de log
            handler = logging.FileHandler(caminho_log)
            handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S"))

            # Adiciona o handler ao logger
            self.logger.addHandler(handler)

        # Registra a mensagem no log
        mensagem = f"{nome} ({ip}) está {status}"
        self.logger.info(mensagem)

    def adicionar_equipamento(self):
        nome = self.nome_input.text().strip()
        ip = self.ip_input.text().strip()

        if not nome:
            QMessageBox.warning(self, "Erro", "O nome do equipamento não pode estar vazio.")
            return

        if not ip:
            QMessageBox.warning(self, "Erro", "O IP do equipamento não pode estar vazio.")
            return

        if not self.validar_ip(ip):
            QMessageBox.warning(self, "Erro", "O IP informado é inválido.")
            return

        if not self.validar_nome(nome):
            QMessageBox.warning(self, "Erro", "Já existe um equipamento com esse nome.")
            return

        # Se todas as validações passarem, adiciona o equipamento
        self.equipamentos[nome] = ip
        self.status_equipamentos[nome] = {
            'status': "OFFLINE",
            'last_event': "N/A",
            'ping_time': "N/A",
            'historico': []  # Inicializa o histórico
        }
        self.lista_equipamentos.addItem(f"{nome} ({ip})")

        # Inicia o monitoramento para o novo equipamento
        threading.Thread(target=self.monitorar_equipamento, args=(nome, ip), daemon=True).start()

        # Salva os dados no arquivo JSON
        self.salvar_dados()

        # Limpa os campos de entrada
        self.nome_input.clear()
        self.ip_input.clear()

    def remover_equipamento(self):
        item = self.lista_equipamentos.currentItem()
        if item:
            nome = item.text().split(" ")[0]
            self.equipamentos.pop(nome, None)
            self.status_equipamentos.pop(nome, None)
            self.lista_equipamentos.takeItem(self.lista_equipamentos.row(item))

            # Salva os dados no arquivo JSON
            self.salvar_dados()

    def abrir_monitoramento(self):
        self.monitoramento_tela = TelaMonitoramento(self.equipamentos, self.status_equipamentos, self.log_file_path)
        self.monitoramento_tela.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_admin = TelaAdministracao()
    tela_admin.show()
    sys.exit(app.exec_())