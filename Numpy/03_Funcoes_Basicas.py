"""
## Aplicações do dia a dia

Vamos supor que você trabalha em uma empresa de vendas e tem os preços de diferentes produtos em uma lista.
Você quer aumentar o preço de todos os produtos em 10%. Com NumPy, isso é simples.
"""

import numpy as np

# Preços dos produtos
precos = np.array([20, 25, 30, 35, 40])

# Aumentar os preços em 10 % (ex.: ajuste de inflação)
novos_precos = precos * 1.10
print(novos_precos)

"""
## np.sum()

NumPy vem com muitas funções úteis. Por exemplo, você pode usar a função `sum()` para somar todos os elementos de um array. 
Isso pode ser útil para somar todas as vendas de um dia, por exemplo.
"""

# Vendas do dia
vendas = np.array([200, 220, 250, 210, 300])

# Somar todas as vendas
total_vendas = np.sum(vendas)
print(total_vendas)

"""
## np.mean()

A função `mean()` é usada para calcular a média de um array. 
Por exemplo, se você quiser calcular a média de vendas diárias em uma semana.
"""

# Vendas diárias em uma semana
vendas = np.array([200, 220, 250, 210, 300, 280, 230])

# Calcular a média de vendas
media_vendas = np.mean(vendas)
print(media_vendas)

"""
## np.max() e np.min()

As funções `max()` e `min()` são usadas para encontrar o valor máximo e mínimo em um array, respectivamente. 
Por exemplo, para encontrar o produto mais caro e mais barato.
"""

# Preços dos produtos
precos = np.array([20, 25, 30, 35, 40])

# Encontrar o produto mais caro e mais barato
produto_mais_caro = np.max(precos)
produto_mais_barato = np.min(precos)
print(produto_mais_caro, produto_mais_barato)

"""
## np.sort()

A função `sort()` é usada para ordenar os elementos de um array. 
Por exemplo, para ordenar as vendas diárias.
"""
# Vendas diárias
vendas = np.array([200, 220, 250, 210, 300])

# Ordenar as vendas
vendas_ordenadas = np.sort(vendas)
print(vendas_ordenadas)


"""
## np.dot()

A função `np.dot()` é usada para calcular o produto escalar de dois arrays. Por exemplo, 
em uma empresa de varejo, você pode querer calcular o valor total de vendas, 
dado o número de cada produto vendido e o preço de cada produto.
"""

# Número de produtos vendidos
quantidades = np.array([10, 20, 30, 40])

# Preços dos produtos
precos = np.array([5, 10, 15, 20])

# Calcular o valor total de vendas?
print(quantidades * precos)
print(np.sum(quantidades * precos))

# Multiplica uma lista pela outra, e faz a total dos valores.
total_vendas = np.dot(quantidades, precos)
print(total_vendas)
