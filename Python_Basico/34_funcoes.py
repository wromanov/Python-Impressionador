# Funções no Python
# 1 - A variável numa função é de escopo local.
# 2 - O retorno é a resposta de uma função.
# 3 - Após o return nada mais é executado.
# 4 - As funções ficam no ínicio do código

# Definindo a Função
def minha_funcao(valor1, valor2):
    soma = valor1 + valor2
    return soma


# Ao atribuir uma função a uma variável, ela automaticamente é chamada.

soma = minha_funcao(1, 2)

print(soma)
