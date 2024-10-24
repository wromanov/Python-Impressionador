"""
## Exercício 1

Você é um gerente de vendas e possui os dados de vendas de um produto para os últimos 7 dias numa lista
: `[127, 90, 201, 150, 210, 220, 115]`. Calcule a média de vendas durante a semana.
"""
import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]

media = np.mean(np.array(dados))

print(f'A media de vendas dos últimos 7 dias foi de {media}.')

"""
## Exercício 2

Você é um analista financeiro e tem os preços de fechamento diário de uma ação para a última semana em um array NumPy:
preços = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50]). 
Calcule o preço máximo, mínimo e a variação de preço durante a semana.
"""

precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])
precos_max = precos.max()
precos_min = precos.min()

print(f'O maior preço foi {precos_max}.')
print(f'O menor preço foi {precos_min}.')

"""
## Exercício 3

Sua loja vendeu em um dia 5 unidades do *Produto A*, 3 unidades do *Produto B* e 2 unidades do *Produto C*. 
Os preços dos produtos são, respectivamente, 100, 200 e 50 reais. Calcule o total de vendas do dia.
"""

quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])

produto_escalavel = np.dot(quantidades, precos)

total_produtos = quantidades * precos

print(f'A quantidade de produtos vendidos foi de {quantidades.sum()} unidades.')
print(f'O valor total de produtos vendidos foi R$ {produto_escalavel}')
