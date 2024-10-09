# Quantidade Indefinidas de Argumentos
# Utilidade:
# Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.
# Estrutura:

"""
*args para positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...

**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ...

##Ordem dos Argumentos
- Sempre os argumentos posicionais vem antes dos keywords argumentos.
- Sempre os argumentos individuais vem antes dos múltiplos argumentos.

def minha_funcao(arg1, arg2, arg3, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):
"""

def minha_soma(*numeros):
    print(numeros) # Tupla
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
print(minha_soma(10, 13, 1, 10, 90, 0, 9, 8))

def preco_final(preco, **adicionais):
    print(adicionais) # Dicionáio
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco
print(preco_final(1000, desconto=0.1, garantia_extra = 100, imposto=0.3))

