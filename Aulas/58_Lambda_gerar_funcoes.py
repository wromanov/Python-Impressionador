"""
# Lambda Expressions para gerar funções

### Descrição

- Uma das aplicações de lambda expressions, além da vista na aula passada, é criar um "gerador de funções".
Nesse caso, usaremos a lambda expressions dentro da definição de uma outra função.

"""


### Exemplo:

# 1. Vamos criar uma função que me permita calcular o valor acrescido do imposto de diferentes categorias (produto, serviço, royalties, etc.)
def calcular_imposto(imposto):
    return lambda preco: preco * (1 + imposto)


# produto 0.1
# serviço 0.15
# royalties 0.25

# Inserindo funções dentro de variáveis - definindo as funções que calculam o imposto das 3 categorias (produto, serviço, royalties)
calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

# Agora vamos aplicar com um valor de nota fiscal de 100 para ver o resultado

print(int(calcular_preco_produto(100)))
print(int(calcular_preco_servico(100)))
print(calcular_preco_royalties(100))