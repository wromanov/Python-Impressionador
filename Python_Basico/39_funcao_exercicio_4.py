# # Exercícios
#
# ### Antes de irmos para o desafio que apresentamos na última aula (que é bem mais complexo do que um exemplo simples) vamos resolver um exercício um pouco mais simples para treinar
#
# ## 1. Cálculo do Percentual e da Lista de Vendedores
#
# - Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta (para eu não precisar calcular manualmente depois)
# - Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas: uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta.

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}


def meta_alcancada(lista, meta):
    bateu_meta = []
    for vendedor in lista:  # vendedor é a chave do dicionário
        valor = lista[vendedor]
        if valor >= meta:
            bateu_meta.append(vendedor)
    quantidade_funcionarios = len(lista)
    quantidade_funcionarios_bateu = len(bateu_meta)
    percentual_bateu_meta = quantidade_funcionarios_bateu / quantidade_funcionarios
    return bateu_meta, percentual_bateu_meta

    # return (f'Colaboradores que bateram a meta: {bateu_meta}\n'
    #         f'Percentual de colaboradores que bateram a meta: {percentual_bateu_meta:.2%}.')


# print(meta_alcancada(vendas, meta))

# desempacotando o return para usar as variaveis
bateu_meta, perc_bateu_meta = meta_alcancada(vendas, meta)

print(f'Colaboradores que bateram a meta: {bateu_meta}.')
print(f'Percentual de colaboradores que bateram a meta: {perc_bateu_meta :.1%}.')
