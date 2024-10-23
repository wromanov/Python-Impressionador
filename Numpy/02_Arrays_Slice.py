"""
## Arrays

Um array é uma estrutura de dados que armazena valores do mesmo tipo. Em Python,
isso é uma grande vantagem porque economiza espaço e permite operações mais eficientes. Vamos criar um array.
"""

# Criação de um array

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

print(array[0])

print(array[1:4])

print(array[0:-1])

print(array[0:-1:2])

print(array[0::2])

print(array[::2])

print(array[::])

print(array[::-1])