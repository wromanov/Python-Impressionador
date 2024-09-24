"""### Tratando a condição falsa:
Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das vezes queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Nesse caso usaremos:

if condição:
    o que eu quero fazer caso a condição seja verdadeira
else:
    o que eu quero fazer caso a condição seja falsa

Voltando ao nosso Exemplo Real da Amazon e do Iphone, agora nossa programa deve avisar nos 2 casos:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades"
- Se ele não bateu a meta do mês, devemos exibir a mensagem: "Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades"
"""

meta = 50000
qtde_vendida = 15000

if qtde_vendida > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendida))
else:
    print('Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades'.format(qtde_vendida, meta))


#
# ## Exemplo
# Vamos fazer um novo exemplo abaixo:
#
# Digamos que você precisa criar um programa para um fundo de investimentos,
# conseguir avaliar o resultado de uma carteira de ações e o quanto de taxa deverá ser pago.
#
# A regra desse fundo de investimentos é:
#
# - O fundo se compromete a entregar no mínimo 5% de retorno ao ano.
# - Caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores.
# - Caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa dos seus investidores.
# - Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores.
#


meta = 0.05
taxa = 0
rendimento = 0.25

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print('A taxa foi de {}'.format(taxa))
    else:
        taxa = 0.02
        print('A taxa foi de {}'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))