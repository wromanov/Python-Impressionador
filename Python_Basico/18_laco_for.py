

# Introdução Laço For

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
nome = 'Walace'

# Percorrendo lista
#for c in range(0, tamanho):
    #print(produtos[c], producao[c])

# Percorrendo String
for letra in nome:
    print(letra)

# Percorrendo uma lista
for item in produtos:
    print(f'Produtos {item}')

# For + If
qnt_func = len(vendas)
qnt_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        print(f'Vendas maior (+) que a meta {venda}')
        qnt_bateu_meta += 1

print(f'Percentual de pessoas que bateram a menta foi de {qnt_bateu_meta / qnt_func:.1%}.')