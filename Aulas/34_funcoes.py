# Funções no Python
# 1 - A variável numa função é de escopo local.
# 2 - O retorno é a resposta de uma função.
# 3 - Após o return nada mais é executado.

def minha_funcao():
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    soma = valor1 + valor2
    return soma


# Ao atribuir uma função a uma variável, ela automaticamente é chamada.

soma = minha_funcao()

print(soma)
