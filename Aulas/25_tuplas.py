"""
# Tuplas

##Estrutura:
tupla = (valor, valor, valor, ...)

### Diferença
Parece uma lista, mas é imutável.

### Vantagens:
- Mais eficiente (em termos de performânce)
- Protege a base de dados (por ser imutável)
- Muito usado para dados heterogêneos

"""

### Criando tuplas
vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
print(vendas)

### Acessando tuplas
vendas[3] = 3000

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]
