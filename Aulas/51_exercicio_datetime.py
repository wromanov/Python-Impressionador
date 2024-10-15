from datetime import datetime

data_nascimento_usuario = input('Informe sua data de nascimento: (dd/mm/aaaa): ')

data_atual = datetime.now()

# Convertendo string em uma data válida
data_nascimento_usuario = datetime.strptime(data_nascimento_usuario, '%d/%m/%Y')

# Formatando a data de Nascimento
data_nascimento_formatada = datetime.strftime(data_nascimento_usuario, '%d/%m/%Y')

dia_nascimento_usuario = data_nascimento_usuario.day
mes_nascimento_usuario = data_nascimento_usuario.month
ano_nascimento_usuario = data_nascimento_usuario.year

dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year

diferenca1 = data_atual - data_nascimento_usuario
print(diferenca1.days / 365)

diferenca2 = ano_atual - ano_nascimento_usuario
print(diferenca2)


