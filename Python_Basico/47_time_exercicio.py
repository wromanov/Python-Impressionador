"""
## Contagem regressiva

Um evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0,
com uma pausa de um segundo entre cada número.
"""

import time
import locale

# for i in range(10, 0, -1):
#     print(i, end=' \r')
#     time.sleep(1)
# print("O evento começou!")

"""
## Formatação de tempo

Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, 
dia do mês de mês do ano, horas:minutos". Crie um script Python que mostra a data e a hora atuais neste formato.
"""


# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_em_struct)

print(f"Data e hora atuais: {tempo_formatado}")

quociente, modulo = divmod(7, 2)

print(f'Divisao: 7/2 |Quociente: {quociente}| Modulo: {modulo}|')

