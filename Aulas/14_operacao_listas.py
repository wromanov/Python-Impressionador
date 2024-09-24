lista_produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
lista_estoque = [100, 150, 100, 120, 70, 180, 80]

#Descobrindo a posição de um item numa lista.
# item_index = produtos.index('tv')
# print(f"O produto {produtos[item_index]} está na posição {item_index} da lista, e possui {estoque[item_index]} unidades em estoque.")

"""Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, 
caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a 
quantidade de unidades em estoque do produto

produto = input("Informe o produto para pesquisa: ").lower().strip()

if produto in lista_produtos:
    item_index = lista_produtos.index(produto)
    print(f"O produto {lista_produtos[item_index]} está na posição {item_index} da lista, e possui {lista_estoque[item_index]} unidades em estoque.")
else:
    print(f"O produto {produto} não existe no estoque.")
"""

"""Adicionado e Removendo Itens de uma Lista."""

#Adicionando item no final da lista
lista_produtos.append('Microondas')
print(lista_produtos)

#Removendo Item do final da lista
lista_produtos.pop()
print(lista_produtos)

#Removendo Item da lista pelo índice
produto_removido = lista_produtos.pop(0) #podemos colocar o pop dentro de uma váriavel para exibir o produto removido.
print(f'Produto removido "{produto_removido}", lista de produtos: {lista_estoque}')

#Removendo Item da lista pelo nome do item
lista_produtos.remove('celular')
print(lista_produtos)

