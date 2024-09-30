# Desempacotando Tuplas

vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
vendas2 = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

# Atribuindo variáveis a tuplas
nome, data_contratacao, data_nascimento, salario, cargo = vendas

print(nome, data_contratacao, data_nascimento, salario, cargo, cargo)


# Percorrendo Tupla
for i, venda in enumerate(vendas2):
    print('O Colaborar "{}" vendeu "{}" unidades'.format(funcionarios[i], venda))
