# Print, split e Join em listas

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
vendidos = 'Arroz, Feijão, Abacate, Nabo, Rabanete, Canjica, Linguiça'

# Join usa um delimitar para separar os itens na lista
print(' '.join(produtos))

# faz cada item aparecer numa linha
print('\n'.join(produtos))

# o métido list transforma uma string em uma lista, utilizando um delimitar passado.
nova_lista = vendidos.split(', ')
print(nova_lista)

# Outros Métodos de incremento em lista
nova_lista += ['Paçoca']
nova_lista = nova_lista + ['Batata']

print(nova_lista)

# Copiando lista da forma certa.

lista_desejos = ['Carro', 'Dinheiro', 'Saúde']

lista_copiada = lista_desejos.copy()
#ou
lista_copiada2 = lista_desejos[:]
