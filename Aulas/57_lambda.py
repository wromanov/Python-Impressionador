# lambda é uma função de uma linha só.

# Variavel lambda argumento: operação


f = lambda num, num2: num * num2

print(f(10, 10))

# A principal utilidade de uma lambda expression é usá-la como argumento de uma outra função, como map e filter.

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000,
                    'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

print(preco_tecnologia.items())

g = lambda preco: preco * 1.30

nova_lista = list(map(g, preco_tecnologia.values()))

print(nova_lista)
