
"""
Índice positivo e negativo

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
+ 0   1   2   3   4  5  6  7  8  9 10 11 12 13

Pegar um item de uma string: texto[índice]
Pegar o tamanho de um texto: len(texto)
"""

email = 'lira@gmail.com'
nome = 'João Lira'

print(len(email))
print(email[:-10])


# Operações com String
# str -> transforma número em string
# in -> verifica se um texto está contido dentro do outro
# operador + -> concatenar string
# format e {} -> substitui valores
# %s -> substitui textos
# %d -> substitui números decimais

faturamento = 1000
custo = 500
lucro = faturamento - custo

#Uso do str() e do concatenar com +

print ('O faturamento da loja foi de: ' + str(faturamento))

###Uso do Format

print('O faturamento foi de: {} '.format(faturamento))

###Uso do %s e %d

print ('O faturamento foi de: %d' % (faturamento))

###Uso do in (mais exercícios práticos nas próximas aulas)

print('@' in 'lira@gmail.com')
print('@' in 'lira.gmail.com')