# ## Estrutura:
#
# - Normalmente usamos a estrutura texto.método() para fazer as modificações que queremos
# - Alguns métodos pedem "argumentos", que são informações que temos que passar para a fórmula (método)
# para ela funcionar. Esses argumentos são passados dentro do parênteses
#
# ## Como usar:
#
# Não decore os métodos, os que você for mais usando com o tempo você vai decorar o que precisar.
#
# Mas a dica é: use essa lista para consulta e busque entender como os métodos funcionam e suas aplicações,
# para poder consultar e usar quando precisar.

#capitalize() -> Coloca a 1ª letra Maiúscula
texto = 'lira'
print(texto.capitalize())


#casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
texto = 'Lira'
print(texto.casefold())


#count()	-> Quantidade de vezes que um valor aparece na string
texto = 'lira@yahoo.com.br'
print(texto.count('.'))


#endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False
texto = 'lira@gmail.com'
print(texto.endswith('gmail.com'))


#find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
texto = 'lira@gmail.com'
print(texto.find('@'))

"""Obs: lembrando como funciona a posição nas strings, então o @ está na posição 4
l i r a @ g m a i l  .  c  o  m
0 1 2 3 4 5 6 7 8 9 10 11 12 13"""

#format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.
faturamento = 1000
print('O faturamento da loja foi de {} reais'.format(faturamento))

#isalnum() -> Verifica se um texto é feito com caracteres alfanuméricos (letras e números)
# -> letras com acento ou ç são considerados letras para essa função.
texto = 'João123'
print(texto.isalnum())

#Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False

#isalpha() -> Verifica se um texto é todo feito de letras.
texto = 'João'
print(texto.isalpha())

#Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, porque 123 não são letras.

#isnumeric()	-> Verifica se um texto é todo feito por números.
texto = '123'
print(texto.isnumeric())

#Obs: existem os métodos isdigit() e isdecimal() que tem variações pontuais em caracteres
# especiais tipo textos com frações e potências, mas para 99% dos casos eles não vão ser necessários.

#replace() -> Substitui um texto por um outro texto em uma string.
texto = '1000.00'
print(texto.replace('.', ','))

#Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que você quer trocar.
# O 2º é o texto que você quer colocar no lugar daquele texto que você está tirando.

#split()	-> Separa uma string de acordo com um delimitador em vários textos diferentes.
texto = 'lira@gmail.com'
print(texto.split('@'))


#splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto
texto = '''Olá, bom dia
        Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
        Faturamento = R$2.500,00
        '''
print(texto.splitlines())

# startswith() -> Verifica se a string começa com determinado texto
texto = 'BEB123453'
print(texto.startswith('BEB'))


#strip()	-> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final
texto = ' BEB123453 '
print(texto.strip())

#title() -> Coloca a 1ª letra de cada palavra em maiúscula
texto = 'joão paulo lira'
print(texto.title())

#upper()	-> Coloca o texto todo em letra maiúscula
texto = 'beb12343'
print(texto.upper())


