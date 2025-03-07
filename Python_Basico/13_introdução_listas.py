"""
# Listas em Python

## Estrutura:

lista = [valor, valor, valor, valor, ...]

lista[i] -> é o valor de índice i da lista.
Obs: Lembre que no python o índice começa em 0, então o primeiro item de uma lista é o item lista[0]

Para substituir um valor de uma lista você pode fazer:
lista[i] = novo_valor

Listas de Produtos de uma Loja:
"""

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

"""Lista de Unidades Vendidas de cada Produto da Loja"""

vendas = [1000, 1500, 350, 270, 900]

print(f'Vendas do produto "{produtos[3]}" foram de "{vendas[3]}" unidades.')

"""### Nesse caso, as listas funcionam da seguinte forma:

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
              0 ,      1   ,    2   ,     3    ,     4   
vendas = [  1000,    1500  ,   350  ,    270   ,    900  ]

"""

texto = 'lira@gmail.com'