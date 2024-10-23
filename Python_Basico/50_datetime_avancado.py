"""
## datetime.datetime.strftime()

A função "strftime()" converte um objeto datetime para uma string de acordo com um formato específico.

Símbolos que podem ser usados para formatar datas podem ser achados
[aqui](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

"""

from datetime import datetime, timezone, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

agora = datetime.now()

data_formatada = agora.strftime('%A, %d/%m/%Y %H:%M:%S')
data_formatada2 = agora.strftime('%A, %d de %B de %Y %H:%M:%S')

print(f'Data formatada modelo 1: {data_formatada}')
print(f'Data formatada modelo 2: {data_formatada2}')

"""
## datetime.datetime.strptime()

A função `strptime()` analisa uma string representando uma data e hora de acordo com um formato. O retorno é um objeto datetime.
"""

# formato DD/MM/YYYY
string_data = "09/06/2023, 15:30:20"
formato = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}")

# formato MM/DD/YYYY
string_data2 = "09/06/2023, 15:30:20"
formato2 = "%m/%d/%Y, %H:%M:%S"
data2 = datetime.strptime(string_data2, formato2)

print(f"Data: {data2}")

"""
## Trabalhando com fuso horário

Podemos criar um objeto datetime usando a classe `datetime`. O construtor da classe aceita os seguintes argumentos:

- year: ano (por exemplo, 2023)
- month: mês (1-12)
- day: dia (1-31)
- hour: hora (0-23)
- minute: minuto (0-59)
- second: segundo (0-59)
- microsecond: microssegundo (0-999999)
- tzinfo: fuso horário

# Hora UTC
Os horários que vimos até o momento são os que chamamos de ingênuos (*naive*). Eles não possuem informações sobre o fuso horário. 
Para criar um horário consciente (*aware*), precisamos passar um objeto `tzinfo` para o construtor da classe `datetime`. 
O módulo `datetime` fornece uma classe `timezone` que pode ser usada para criar um objeto `tzinfo`. No exemplo abaixo, usamos UTC como fuso horário. UTC significa Tempo Universal Coordenado, que é o fuso horário de referência a partir do qual todos os outros fusos horários são calculados.

![UTC](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/World_Time_Zones_Map.png/800px-World_Time_Zones_Map.png)
"""

fuso_horario = timezone.utc
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario)
print(f"Data/hora: {data_hora}")

# Podemos passar um objeto timedelta para o construtor da classe timezone
# para criar um fuso horário com um deslocamento específico.
# Por exemplo, o código abaixo cria um fuso horário com um deslocamento de 3 horas em relação ao UTC:

# exemplo com fuso horário de São Paulo


fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")

"""
Como alternativa, podemos usar o módulo "zoneinfo" para criar um objeto "tzinfo". 
O módulo "zoneinfo" está disponível na biblioteca padrão do Python desde a versão 3.9. 
O módulo "zoneinfo" fornece uma classe "ZoneInfo" que pode ser usada para criar um objeto "`tzinfo". 
No exemplo abaixo, usamos o fuso horário de São Paulo. Observe que não precisamos passar um objeto "timedelta" 
para o construtor da classe "ZoneInfo".
"""
import pytz

fuso_horario_sao_paulo = pytz.timezone('America/Sao_Paulo')
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")

# Definir o fuso horário local (exemplo: São Paulo)
fuso_horario_sao_paulo = pytz.timezone("America/Sao_Paulo")

# Definir o fuso horário local (exemplo: Nova York)
fuso_horario_new_york = pytz.timezone("America/New_York")

# Obter a data e hora atuais e ajustar para o fuso horário local
data_hora_local = datetime.now().astimezone(fuso_horario_sao_paulo)
data_hora_new_york = datetime.now().astimezone(fuso_horario_new_york)

# Exibir a data/hora no formato desejado, incluindo o fuso horário
print(data_hora_local.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
print(data_hora_new_york.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
