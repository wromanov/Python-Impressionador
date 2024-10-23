"""
## time.strftime()

A função strftime() converte um objeto de tempo struct para uma string de acordo com um formato específico.

Os símbolos de formato que podem ser usados estão disponíveis na documentação oficial do Python,
[neste link](https://docs.python.org/3/library/time.html#time.strftime).

Por exemplo, podemos querer uma string de tempo no seguinte formato:
"Dia da semana, dia do mês de mês do ano, horas:minutos:segundos". Podemos usar o seguinte código para obter o tempo formatado:
"""
import time
import locale

# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
print(tempo_em_struct)

print(time.strftime("%d %B %Y", tempo_em_struct))

print(time.strftime("%H:%M:%S", tempo_em_struct))

tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)

print(f"Tempo formatado: {tempo_formatado}")

"""
## time.strptime()

A função `strptime()` analisa uma string representando um horário de acordo com um formato. O retorno é um objeto `struct_time`.

string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")
"""

#Padrão Brasil
string_tempo = "06/09/2023"
formato = "%d/%m/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")

#Padrão USA
string_tempo = "06/09/2023"
formato = "%m/%d/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")