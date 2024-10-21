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
    print(numeros)  # Tupla
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(minha_soma(10, 13, 1, 10, 90, 0, 9, 8))


def preco_final(preco, **adicionais):
    print(adicionais)  # Dicionáio
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco


print(preco_final(1000, desconto=0.1, garantia_extra=100, imposto=0.3))


def compra_acoes(nome, *compras, **investimentos):
    if 'papel' in investimentos:
        print('Cliente', nome, 'comprou R$', sum(compras), 'em', investimentos['papel'], 'e foram feitas', len(compras),
              'operações')
    else:
        print('Cliente', nome, 'não quer comprar ações')


compra_acoes('José Pereira', 100, 200, 100, 50, 35, papel='WEGE3')


"""### **Regras gerais**

1. Os argumentos que não recebem pré-definição vêm sempre antes

  Por exemplo:

  `def numeros (a, b, c = 1, d = 2)`


2. Os args sempre precedem os kwargs

  Por exemplo:

  `def numeros (*args, **kwargs)`

3. Se a função tiver tudo isso, primeiro passamos os argumentos sem valores pré-definidos, depois aqueles que possuem pré-definição, depois args e depois kwargs

  Por exemplo:

  `def numeros (a, b, c = 1, d = 2, *args, **kwargs)`
"""