"""
# Guia para o módulo datetime em Python

O módulo datetime em Python fornece classes para manipulação de datas e horas.
Aqui está um guia simples para algumas das funções mais úteis deste módulo.
"""

from datetime import datetime
from datetime import date

# A função `now()` retorna a data e a hora atuais.
agora = datetime.now()
print(f"Agora: {agora}")

# Retorna apenas a data
print(f"Data: {agora.date()}")

# Retorna apenas a hora
print(f"Horário: {agora.time()}")

print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")

## datetime.date.today() retorna a data atual.
hoje = date.today()
print(f"Data atual: {hoje}")

print(f"Ano: {hoje.year}")
print(f"Mês: {hoje.month}")
print(f"Dia: {hoje.day}")