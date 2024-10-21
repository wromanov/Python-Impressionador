## 12. List Comprehension

# Forma de criar listas a partir de outras listas, baseadas em loops com uma estrutura de código mais resumida do que os "for" tradicionais.

"""
Imagine que precisamos realizar a tarefa de transformar cada caractere na string acima em um item separado dentro de uma nova lista.
Como feríamos isso com nosso conhecimento em Python até agora?

"""
acao = 'MGLU3'
lista_caracteres = []
for item in acao:
    lista_caracteres.append(item)
    print(lista_caracteres)

# E como fazer isso utilizando a compreensão de lista?

metodo_list_comprencao = [item for item in acao]

print(metodo_list_comprencao)

# Imagine que você recebeu uma série de tickers que vieram incompletos. Antes de realizar sua rotina,
# precisa adicionar um número '3' aos nomes dos papéis. Como você faria?

ativos = ['MGLU', 'VALE', 'WEGE', 'LREN']
novo_ativos = []
for ativo in ativos:
    novo_ativos.append(ativo + '3')
    print(novo_ativos)

# Podemos realizar essa tarefa com uma compreensão de lista de uma forma mais rápida.

ativos2 = [ativo + '3' for ativo in ativos]
print(ativos2)

# Imagine que quiséssemos elevar todos os números de 0 a 10 ao quadrado.
# Da forma tradicional, faríamos:

lista_numeros = []
for elemento in range(0,11):
    lista_numeros.append(elemento**2)
    print(lista_numeros)

lista_numeros2 = [elemento**2 for elemento in range(0,11)]


# Adicione um ".SA" ao fim de cada papel

acoes = "ITUB4 MGLU3 MLAS3 PRIO3 PETR4 VALE3 WEGE3 POSI3"
acoes_modificadas = acoes.split(' ')
acoes2 = [f'{papel}.SA' for papel in acoes_modificadas]
print(acoes2)


# Um exemplo prático de List Comprehension
### O que faríamos se quisermos ordenar 2 listas "relacionadas"

vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']
meta = 1000

# Transforma as duas listas em uma tupla com os itens relacionados
lista_aux = list(zip(vendas_produtos, produtos))

# Ordena a lista do menor para o maior
lista_aux.sort(reverse=True)

# Faz o upacking da tupla, e coloca o nome dos produtos na lista
produtos = [produto for vendas, produto in lista_aux]

print(produtos)

# List Comprehensions com if para "filtrar" itens
# Estrutura
# lista = [expressão for item in iterable if condição]

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)