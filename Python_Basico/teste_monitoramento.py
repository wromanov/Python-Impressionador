import os
import time
import datetime
import threading
import subprocess
import platform

# Lista de equipamentos com seus respectivos IPs
equipamentos = {
    "Meu Computador": "192.168.1.24",
    # Adicione mais equipamentos conforme necessário
}

# Dicionário para armazenar o status dos equipamentos
status_equipamentos = {}

# Determina o comando de ping apropriado
sistema = platform.system()
if sistema == "Windows":
    comando_ping = "ping -n 1 -w 1000 {}"
else:
    comando_ping = "ping -c 1 -W 1 {}"


def registrar_log(nome, ip, status):
    """Registra eventos no log com separação diária."""
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
    nome_arquivo = f"log_monitoramento_{data_atual}.log"
    mensagem = f"{timestamp} - {nome} ({ip}) está {status}\n"

    with open(nome_arquivo, "a") as log:
        log.write(mensagem)

    print(mensagem.strip())


def verificar_conectividade(nome, ip):
    """Executa um ping para verificar a conectividade do equipamento."""
    resultado = subprocess.run(comando_ping.format(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return resultado.returncode == 0


def monitorar_equipamento(nome, ip):
    """Monitora continuamente um equipamento."""
    while True:
        conectado = verificar_conectividade(nome, ip)
        status_atual = "ONLINE" if conectado else "OFFLINE"

        if nome not in status_equipamentos or status_equipamentos[nome] != status_atual:
            status_equipamentos[nome] = status_atual
            registrar_log(nome, ip, status_atual)

        time.sleep(5)  # Intervalo de 60 segundos entre as verificações


def iniciar_monitoramento():
    """Inicia a monitoração de todos os equipamentos em threads separadas."""
    threads = []
    for nome, ip in equipamentos.items():
        thread = threading.Thread(target=monitorar_equipamento, args=(nome, ip), daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    iniciar_monitoramento()
