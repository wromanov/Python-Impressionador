"""
### Exemplo:

Vamos criar um programa para analisar o bônus dos funcionários de uma empresa (pode parecer "simples",
mas uma empresa como a Amazon tem 900.000 funcionários)

Para os cargos de vendedores, a regra do bônus é de acordo com a meta de vendas da pessoa:

Se ela vendeu abaixo da meta dela, ela não ganha bônus.

Se ela vendeu acima da meta dela, ela ganha como bônus 3% do valor que ela vendeu.

Se ela vendeu mais do que o dobro da meta dela, ela ganha como bônus 7% do valor que ela vendeu.

Vamos criar um programa para avaliar uma pessoa que tinha como meta de vendas 20.000 reais e calcular o bônus dela,
 de acordo com o valor de vendas que ela tiver.
"""

meta = 20000
vendas = 15000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print('Ganhou {} de bônus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print('Ganhou {} de bônus'.format(bonus))