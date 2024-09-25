# #Ordenar Listas e Juntar Listas

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']
valores1 = [15, 20, 25, 35, 45]
valores2 = [35, 22, 40, 35, 45]

#Juntar Listas - método 1
produtos.extend(novos_produtos)
print(produtos)

# Juntar Lista método 2
# nova_lista = produtos + novos_produtos
# print(nova_lista)

#Inserir uma lista dentro da outra
# produtos.append(novos_produtos)
# print(produtos)

#Somando itens de uma lista
print(valores1[1] + valores2[3])

#Ordenar listas em ordem alfabetica, sendo que letras maiusculas tem precedencia.
print(produtos.sort())
