"""
### Exemplo

Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um to do.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.
- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um to do, o funcionário não ganha bônus.
"""

meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 0

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')


nota_funcionario = 5
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')