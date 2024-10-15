"""
# Filter

De forma análoga ao "map", a função "filter" aplica um filtro a vários elementos de uma lista de uma só vez.
"""

# Crie uma função para filtrar os números pares de uma lista.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def verifica_par(valor):
    if valor % 2 == 0:
        return True


numeros_pares = list(filter(verifica_par, lista_numeros))

print(numeros_pares)

# Crie uma função que verifique se os papíes de uma outra lista pertence a primeira lista.

ibov = ['ABEV3', 'PETRA4', 'VALE3', 'ITUB4']
lista_papeis = ['ORVR3', 'ABEV3', 'BAUH4', 'JOPA3', 'ITUB4']


def verifica_duplicata(papel):
    return papel in ibov  # vai retornar verdeiro ou falso.


verifica = list(filter(verifica_duplicata, lista_papeis))
print(verifica)
