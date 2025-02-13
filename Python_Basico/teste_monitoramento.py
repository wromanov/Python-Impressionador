import os
import time
import datetime
import threading
import subprocess
import platform

# Lista de equipamentos com seus respectivos IPs
equipamentos = {
    "CD_CHK_A_01": "10.168.250.1",
    "CD_CHK_A_02": "10.168.250.2",
    "CD_CHK_A_03": "10.168.250.3",
    "CD_CHK_A_04": "10.168.250.4",
    "CD_CHK_A_05": "10.168.250.5",
    "CD_CHK_A_06": "10.168.250.6",
    "CD_CHK_A_07": "10.168.250.7",
    "CD_CHK_A_08": "10.168.250.8",
    "CD_CHK_B_01": "10.168.250.9",
    "CD_CHK_B_02": "10.168.250.10",
    "CD_CHK_B_03": "10.168.250.11",
    "CD_CHK_B_04": "10.168.250.12",
    "CD_CHK_B_05": "10.168.250.13",
    "CD_CHK_B_06": "10.168.250.14",
    "CD_CHK_B_07": "10.168.250.15",
    "CD_CHK_B_08": "10.168.250.16",
    "FIDS_CHK_01": "10.168.250.105",
    "FIDS_CHK_02": "10.168.250.106",
    "FIDS_CHK_03": "10.168.250.107",
    "FIDS_CHK_04": "10.168.250.108",
    "FIDS_RXI_01": "10.168.250.109",
    "FIDS_RXD_01": "10.168.250.110",
    "FIDS_ED2_01": "10.168.250.111",
    "FIDS_ED2_02": "10.168.250.112",
    "FIDS_PDI_01": "10.168.250.113",
    "FIDS_PDD_01": "10.168.250.114",
    "LED_RXD_01": "10.168.250.115",
    "LED_RXI_01": "10.168.250.116",
    "LED_RDI_01": "10.168.250.117",
    "LED_REI_01": "10.168.250.118",
    "CD_ED2_A_01": "10.168.250.25",
    "CD_ED2_A_02": "10.168.250.26",
    "CD_ED2_A_03": "10.168.250.27",
    "CD_ED2_A_04": "10.168.250.28",
    "CD_ED2_A_05": "10.168.250.29",
    "CD_ED2_A_06": "10.168.250.30",
    "CD_ED2_A_07": "10.168.250.31",
    "CD_ED2_A_08": "10.168.250.32",
    "CD_ED2_B_01": "10.168.250.33",
    "CD_ED2_B_02": "10.168.250.34",
    "CD_ED2_B_03": "10.168.250.35",
    "CD_ED2_B_04": "10.168.250.36",
    "CD_ED2_B_05": "10.168.250.37",
    "CD_ED2_B_06": "10.168.250.38",
    "CD_ED2_B_07": "10.168.250.39",
    "CD_ED2_B_08": "10.168.250.40",
    "CD_RBD_A_01": "10.168.250.81",
    "CD_RBD_A_02": "10.168.250.82",
    "CD_RBD_A_03": "10.168.250.83",
    "CD_RBD_A_04": "10.168.250.84",
    "CD_RBD_A_05": "10.168.250.85",
    "CD_RBD_A_06": "10.168.250.86",
    "CD_RBD_A_07": "10.168.250.221",
    "CD_RBD_A_08": "10.168.250.222",
    "CD_RBD_B_01": "10.168.250.87",
    "CD_RBD_B_02": "10.168.250.88",
    "CD_RBD_B_03": "10.168.250.89",
    "CD_RBD_B_04": "10.168.250.90",
    "CD_RBD_B_05": "10.168.250.91",
    "CD_RBD_B_06": "10.168.250.92",
    "CD_EIN_A_01": "10.168.250.59",
    "CD_EIN_A_02": "10.168.250.60",
    "CD_EIN_A_03": "10.168.250.61",
    "CD_EIN_A_04": "10.168.250.62",
    "CD_EIN_A_05": "10.168.250.63",
    "CD_EIN_A_06": "10.168.250.64",
    "CD_EIN_A_07": "10.168.250.65",
    "CD_EIN_A_08": "10.168.250.66",
    "CD_EIN_A_09": "10.168.250.67",
    "CD_EIN_A_10": "10.168.250.68",
    "CD_EIN_A_11": "10.168.250.69",
    "CD_EIN_B_01": "10.168.250.70",
    "CD_EIN_B_02": "10.168.250.71",
    "CD_EIN_B_03": "10.168.250.72",
    "CD_EIN_B_04": "10.168.250.73",
    "CD_EIN_B_05": "10.168.250.74",
    "CD_EIN_B_06": "10.168.250.75",
    "CD_EIN_B_07": "10.168.250.76",
    "CD_EIN_B_08": "10.168.250.77",
    "CD_EIN_B_09": "10.168.250.78",
    "CD_EIN_B_10": "10.168.250.79",
    "CD_EIN_B_11": "10.168.250.80",
    "CD_RBI_A_01": "10.168.250.93",
    "CD_RBI_A_02": "10.168.250.94",
    "CD_RBI_A_03": "10.168.250.95",
    "CD_RBI_A_04": "10.168.250.96",
    "CD_RBI_A_05": "10.168.250.97",
    "CD_RBI_A_06": "10.168.250.98",
    "CD_RBI_B_01": "10.168.250.99",
    "CD_RBI_B_02": "10.168.250.100",
    "CD_RBI_B_03": "10.168.250.101",
    "CD_RBI_B_04": "10.168.250.102",
    "CD_RBI_B_05": "10.168.250.103",
    "CD_RBI_B_06": "10.168.250.104",
    "CD_CIN_A_01": "10.168.250.53",
    "CD_CIN_A_02": "10.168.250.54",
    "CD_CIN_A_03": "10.168.250.55",
    "CD_CIN_A_04": "10.168.250.56",
    "CD_CIN_A_05": "10.168.250.57",
    "CD_CIN_A_06": "10.168.250.58",
    "CD_CIN_A_07": "10.168.250.119",
    "CD_CIN_A_08": "10.168.250.220",
    "CD_ED1_A_01": "10.168.250.17",
    "CD_ED1_A_02": "10.168.250.18",
    "CD_ED1_A_03": "10.168.250.19",
    "CD_ED1_A_04": "10.168.250.20",
    "CD_ED1_B_01": "10.168.250.21",
    "CD_ED1_B_02": "10.168.250.22",
    "CD_ED1_B_03": "10.168.250.23",
    "CD_ED1_B_04": "10.168.250.24",
    "CD_CEM_A_01": "10.168.250.41",
    "CD_CEM_A_02": "10.168.250.42",
    "CD_CEM_A_03": "10.168.250.43",
    "CD_CEM_A_04": "10.168.250.44",
    "CD_CEM_A_05": "10.168.250.45",
    "CD_CEM_A_06": "10.168.250.46",
    "CD_CDE_A_01": "10.168.250.47",
    "CD_CDE_A_02": "10.168.250.48",
    "CD_CDE_A_03": "10.168.250.49",
    "CD_CDE_A_04": "10.168.250.50",
    "CD_CDE_A_05": "10.168.250.51",
    "CD_CDE_A_06": "10.168.250.52",
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
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nome_arquivo = f"monitoramento_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

    with open(nome_arquivo, "a") as log_file:
        log_file.write(f"{timestamp} - {nome} ({ip}) - {status}\n")


def verificar_status():
    """Verifica o status dos equipamentos continuamente."""
    while True:
        for nome, ip in equipamentos.items():
            try:
                resposta = subprocess.run(
                    comando_ping.format(ip),
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                esta_online = resposta.returncode == 0
            except Exception as e:
                print(f"Erro ao verificar {nome}: {e}")
                esta_online = False

            if nome not in status_equipamentos:
                status_equipamentos[nome] = {"online": esta_online, "ultima_mudanca": None}

            # Definir um valor padrão para status_texto
            status_texto = "ONLINE" if status_equipamentos[nome]["online"] else "OFFLINE"

            if status_equipamentos[nome]["online"] != esta_online:
                status_equipamentos[nome]["online"] = esta_online
                status_equipamentos[nome]["ultima_mudanca"] = datetime.datetime.now()
                status_texto = "ONLINE" if esta_online else "OFFLINE"
                registrar_log(nome, ip, status_texto)

            ultima_mudanca = status_equipamentos[nome]["ultima_mudanca"]
            ultima_mudanca_texto = ultima_mudanca.strftime("%Y-%m-%d %H:%M:%S") if ultima_mudanca else "N/A"
            print(f"{nome} - {status_texto} (Desde: {ultima_mudanca_texto})")

        print("-" * 50)
        time.sleep(5)



# Executar a verificação em uma thread separada para rodar continuamente
thread = threading.Thread(target=verificar_status, daemon=True)
thread.start()

# Manter o script rodando
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Monitoramento encerrado.")
