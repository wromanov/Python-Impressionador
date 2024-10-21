# lambda é uma função de uma linha só.

# Variável lambda argumento: operação


f = lambda num, num2: num * num2

print(f(10, 10))

# A principal utilidade de um lambda expression é usá-la como argumento de outra função, como map e filter.

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000,
                    'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

# Usa-se lambda para não precisar criar uma função, quando a função faria apenas uma coisa.
# Cria uma nova lista com os valores acrescido de 30%
nova_lista = list(map(lambda preco: preco[1] * 1.30, preco_tecnologia.items()))
print(nova_lista)

# Filtra os valores maiors que 2k
verificar_valores = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))
print(verificar_valores)