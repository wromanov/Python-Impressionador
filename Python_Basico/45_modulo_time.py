# Módulo time em Python

# O módulo time em Python fornece uma variedade de funções para trabalhar com tempo.

## time.time()

# A função time() retorna o tempo atual em segundos desde a Epoch (1º de janeiro de 1970).

import time

# Tempo em segundos
tempo_atual_segundos = time.time()

print(f"Tempo atual: {tempo_atual_segundos} segundos desde a Epoch")

# Tempo em nano segundos
tempo_atual_nanosegundos = time.time_ns()

print(f"Tempo atual: {tempo_atual_nanosegundos} nanosegundos desde a Epoch")

# Calcular bachmark de uma aplicação
#
# inicio = time.time()
#
# for i in range(100_000_000):  # 10000000
#     pass
#
# fim = time.time()

# print(f"Tempo decorrido: {fim - inicio} segundos")

# A função "ctime()" converte um tempo expresso em segundos desde a epoch em uma string representando o tempo local.
tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}")

"""
A função "localtime()" converte um tempo expresso em segundos desde a epoch em um objeto struct_time. 
Este objeto contém informações sobre o tempo local, como ano, mês, dia, hora, minuto, segundo, etc. 
A função "localtime()" usa o fuso horário local.
"""

tempo_local_atual = time.localtime(tempo_atual_segundos)

print(f"Tempo local Atual: {tempo_local_atual}")

# Obtém o Ano
print(f'Ano: {tempo_local_atual.tm_year}')

# Obtém a Hora
print(f'Horas: {tempo_local_atual.tm_hour}')

#Obtém os Minutos
print(f'Minutos: {tempo_local_atual.tm_min}')

# Dia da semana (0-6, 0 é segunda-feira, 6 é domingo). Documentação: https://docs.python.org/3/library/time.html#time.struct_time
print(f'Dia da semana: {tempo_local_atual.tm_wday}')

# Dia do ano (1-366).
print(f'Dia do ano: {tempo_local_atual.tm_yday}')

print(f'Time zone: {tempo_local_atual.tm_zone}')

acao = 'ITAU4 MAGALU4'

lista = acao.split(' ')

lista2 = [item + '.SA' for item in lista]
print(lista2)