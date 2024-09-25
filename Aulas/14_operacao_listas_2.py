# Descobrindo o maior e menor valor dentro de uma lista

lista_vendas = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
lista_produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']

mais_vendidos = max(lista_vendas)
menos_vendidos = min(lista_vendas)

print(mais_vendidos)
print(menos_vendidos)

#Descobrindo o indice do produto mais e menos vendidos.

indice_produto_max = lista_vendas.index(mais_vendidos)
indice_produto_min = lista_vendas.index(menos_vendidos)




