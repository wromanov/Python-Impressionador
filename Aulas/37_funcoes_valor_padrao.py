"""
# Valores Padrão para Argumentos
- Vamos criar uma função que padronize códigos de produtos. O default será padronizar os códigos para letras minúsculas (dado por 'm'),
mas se o usuário quiser pode padronizar para maiúscula, dado por ('M').
"""

produtos = ['apple tv', 'mac   ', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']


def padronizar(lista, padrao='m'):
    for indice, produto in enumerate(lista):
        produto = produto.strip()
        produto = produto.replace('  ', ' ')
        if padrao == 'M':
            produto = produto.upper()
        elif padrao == 'm':
            produto = produto.casefold()
        lista[indice] = produto
    return lista


print(padronizar(produtos))
