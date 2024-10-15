"""
O método map() em Python é usado para aplicar uma função a todos os itens de um ou mais iteráveis (como listas ou tuplas)
e retornar um objeto de mapa, que é um iterador. Em outras palavras, ele mapeia os elementos de um iterável para uma função,
retornando os resultados sem precisar de um loop explícito.

# Exemplo

    map(função, iterável)

"""

# Inserindo uma string no final de cada item de uma lista.

acoes = ['BRB', 'STD', 'ADA']


def incrementar_texto(texto):
    texto_modificado = texto + '.SA'
    return texto_modificado


# Necessário envolver o map em um list, para transforma o resultado em uma lista.
acoes_modificadas = list(map(incrementar_texto, acoes))

print(acoes_modificadas)

# Crie uma função que modifique o preço de abertura para vários papéis.
# A função deve modificar o preço adicionado 1% em cima do valor.

precos = [26.78, 78.98, 25.76]


def aplica_retorno(valor):
    valor_transformado = round(valor * 1.01, 2)
    return valor_transformado


precos_modificados = list(map(aplica_retorno, precos))
print(precos_modificados)

# Crie uma função que eleva um número a outro número qualquer.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Observação, o map só suporta função com um argumento, e para esses casos deixamos um argumento padrão.
def potencia_qualquer(numero, potencia=2):
    return numero ** potencia


numero_elevado = list(map(potencia_qualquer, lista_numeros))

print(numero_elevado)
