"""
# Estrutura while:
### Funcionamento:
Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.
A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ela terminar de ser verdadeira, o código "sai" do while.
"""

"""
A pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de venda. 
Enquanto o usuário não encerrar o programa, significa que ele está registrando novos produtos, 
então o programa deve permitir e entrada de quantos produtos o usuário quiser.
"""

venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
vendas = []
#crie aqui o programa

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, '
                  'basta apertar enter com a caixa vazia')

print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

