"""
## datetime.timedelta()

A classe timedelta é usada para realizar operações com datas (adição e subtração).
"""

from datetime import datetime, timedelta

data_atual = datetime.now()
print(f"Data atual: {data_atual}")

data_futura = data_atual + timedelta(days=10)
print(f"Data 10 dias no futuro: {data_futura}")

data_passada = data_atual - timedelta(days=10)
print(f"Data 10 dias no passado: {data_passada}")

dez_horas_adiante = data_atual + timedelta(hours=10)
print(f"10 horas adiante: {dez_horas_adiante}")

"""
## Criação de um objeto datetime

Podemos criar um objeto datetime usando a classe `datetime`. O construtor da classe possui como principais argumentos:

- `year`: ano (por exemplo, 2023)
- `month`: mês (1-12)
- `day`: dia (1-31)
- `hour`: hora (0-23)
- `minute`: minuto (0-59)
- `second`: segundo (0-59)
- `microsecond`: microssegundo (0-999999)
- `tzinfo`: fuso horário
"""

data = datetime(2023, 7, 20, 8, 30, 20)
print(f"Data: {data}")

data = datetime(2023, 7, 20)
print(f"Data: {data}")

# `fromisoformat()` é um método de classe que converte uma string em um objeto datetime.

data_hora_iso = datetime.fromisoformat("2023-06-26 15:30:20")
print(f"Data/hora: {data_hora_iso}")

"""
## Calcular a diferença entre duas datas

Podemos calcular a diferença entre duas datas subtraindo uma da outra. O resultado será um objeto timedelta.
"""

data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

diferenca = data2 - data1
print(f"A diferença entre as duas datas é de {diferenca.days} dias.")

print(type(diferenca))

"""
## Comparação entre datas

Podemos comparar datas usando os operadores de comparação padrão.

Segue uma lógica intuitiva:

    passado < presente < futuro
"""

data1 = datetime(2023, 7, 25)
data2 = datetime(2023, 7, 25)

if data1 > data2:
    print("A data1 é posterior à data2")
elif data1 < data2:
    print("A data1 é anterior à data2")
else:
    print("As datas são iguais")


"""
## Ordenando uma lista de datas

Podemos usar a função `sorted` para ordenar uma lista de datas.
"""

datas = [
    datetime(2023, 6, 28),
    datetime(2023, 5, 28),
    datetime(2023, 7, 28),
    datetime(2023, 6, 18),
]

datas_ordenadas = sorted(datas)

print(datas_ordenadas)

for data in datas_ordenadas:
    print(data.date())