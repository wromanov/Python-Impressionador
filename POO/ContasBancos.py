# Se não tiver nenhum parâmetro na classe, pode remover os parenteses.

# Métodos privados são definidos com underline _

# Padrão de nome de classe é PascalCase
class ContaCorrente:
    def __init__(self, nome, cpf, agencia, conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.cheque_especial = 1000
        self.agencia = agencia
        self.conta = conta

    #Padrão de nome de funções é snake_case
    # 'Underline' Sinaliza que esse o método é 'privado' feito apenas para ser usado dentro da classe.
    def _consultar_limite_conta(self):
        # Retorna o limite do cheque especial
        return self.cheque_especial

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        # Verifica se o saldo cobre o valor do saque
        if self.saldo >= valor:
            self.saldo -= valor

        # Caso o saldo seja insuficiente, mas o valor seja coberto pelo saldo + cheque especial
        elif self.saldo + self._consultar_limite_conta() >= valor:
            # Calcula a parte do saque que o saldo cobre
            diferenca = valor - self.saldo
            self.saldo = 0  # Zera o saldo
            self.cheque_especial -= diferenca  # Subtrai a diferença do cheque especial

        else:
            # Quando nem o saldo e o cheque especial cobrem o saque
            print(f'Saldo insuficiente para saque. Saldo atual: R${self.consultar_saldo()}')

    def consultar_primeiro_nome(self):
        return self.nome.split()[0]

    def consultar_cheque_especial(self):
        return self._consultar_limite_conta()


# Programa
ContaCorrente = ContaCorrente('Walace Delgado', '140.887.137-88', 12345, 33214 )

# Adicionando cheque especial de $$ 1000
# ContaCorrente.limite_conta(1000)

# Realizando Deposito
ContaCorrente.depositar(1500)

# Consultando Saldo
print(f'Olá {ContaCorrente.consultar_primeiro_nome()}, seu saldo atual é R${ContaCorrente.consultar_saldo()}, '
      f'limite de cheque especial R$ {ContaCorrente.consultar_cheque_especial()}.')

# Realizando Saque
ContaCorrente.sacar(1700)

# Consultando Saldo
print(f'Olá {ContaCorrente.consultar_primeiro_nome()}, seu saldo atual é R${ContaCorrente.consultar_saldo()}, '
      f'limite de cheque especial R$ {ContaCorrente.consultar_cheque_especial()}.')
