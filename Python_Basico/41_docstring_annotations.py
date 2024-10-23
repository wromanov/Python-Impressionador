"""
# Docstring e Annotations

# Estrutura - São ferramentas "apenas" para organização:

Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que a gente
precise usar essa mesma função semanas, meses ou até anos depois da sua criação.

Por isso é importante usarmos DocStrings e Annotations

- Docstring - diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor.

- Annotation - diz o que devem ser os argumentos e o que a função retorna

Em muitas empresas, o time de tecnologia vai ter um padrão que você deve seguir para isso, mas caso não tenha, vamos te mostrar um padrão bom a ser utilizado.
"""

# Docstring
def minha_soma(num1, num2, num3):
    """Faz a soma de 3 números inteiros e devolve como resposta um inteiro

    Parameters:
        num1 (int): primeiro número a ser somado
        num2 (int): segundo número a ser somado
        num3 (int): terceiro número a ser somado

    Returns:
        soma (int): o valor da soma dos 3 números dados como argumento
    """
    return num1 + num2 + num3


minha_soma(1, 2, 3)


# Annotations
def minha_multiplicacao(num1: 'primeiro número a ser somado', num2: int, num3: int) -> int:
    return num1 * num2 * num3


minha_multiplicacao(1, 2, 3)
