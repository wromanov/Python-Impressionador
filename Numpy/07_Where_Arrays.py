import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

# Método 1 - List Comprehension - Filtrar Funcionários Acima da Média Salarial
func_acima_media_sal = np.array([valor for valor in salarios if valor > media_salarial])

print(
    f'A média salarial da empresa é de R${media_salarial:.2f} e os salários acima da media são {func_acima_media_sal}.')

# Método 2 - NP Where - Filtrar Funcionários Acima da Média Salarial
func_acima_media_sal_2 = np.where(salarios > media_salarial)

# Retorna o índice dos valores contidos na lista
print(func_acima_media_sal_2)

# Exibir os valores passando com parametro o índice da lista
print(salarios[func_acima_media_sal_2])

# Método 3 - Fazendo o filtro diretamente
print(salarios[salarios > media_salarial])
