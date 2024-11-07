# Se não tiver nenhum parâmetro na classe, pode remover os parenteses.
from datetime import datetime
from random import randint

import pytz


# Métodos privados são definidos com underline _

# Padrão de nome de classe é PascalCase
class ContaCorrente:

    # Métodos estáticos são criados acima dos métodos da classe.
    # Esse tipo de método não usa nenhuma informação da classe, por trata-se de um método auxiliar para outro método dentro da classe.
    @staticmethod  # Indica um método estático
    # Método para consultar hora
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S %p')

    def __init__(self, nome, cpf, agencia, num_conta, __idade):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.cheque_especial = 1000
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.__idade = None  # Ao usar dois underscores o argumento fica indisponível, se tornando privado da classe.
        self.cartoes = []

    # Padrão de nome de funções é snake_case
    # 'Underline' Sinaliza que esse o método é 'privado' feito apenas para ser usado dentro da classe.
    def _consultar_limite_conta(self):
        # Retorna o limite do cheque especial
        return self.cheque_especial

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor
        self.transacoes.append((valor, f'Saldo: {self._saldo}', self._data_hora()))

    def sacar(self, valor):
        # Verifica se o saldo cobre o valor do saque
        if self._saldo >= valor:
            self._saldo -= valor
            self.transacoes.append((-valor, f'Saldo: {self._saldo}', self._data_hora()))

        # Caso o saldo seja insuficiente, mas o valor seja coberto pelo saldo + cheque especial
        elif self._saldo + self._consultar_limite_conta() >= valor:
            # Calcula a parte do saque que o saldo cobre
            diferenca = valor - self._saldo
            self._saldo = 0  # Zera o saldo
            self.cheque_especial -= diferenca  # Subtrai a diferença do cheque especial
            self.transacoes.append((-valor, f'Saldo: {self._saldo}', self._data_hora()))

        else:
            # Quando nem o saldo e o cheque especial cobrem o saque
            print(f'Saldo insuficiente para saque. Saldo atual: R${self.consultar_saldo()}')

    def consultar_primeiro_nome(self):
        return self.nome.split()[0]

    def consultar_cheque_especial(self):
        return self._consultar_limite_conta()

    def consultar_transacoes(self):
        print('### Histórico de Transações ###')
        for transacoes in self.transacoes:
            print(transacoes)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, f'Saldo: {self._saldo}', ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, f'Saldo: {conta_destino._saldo}', ContaCorrente._data_hora()))

    def consultar_idade(self):
        return self.__idade


# Relacionado Classes
class CartaoCredito:
    """
        Métodos estáticos são funções da classe que não dependem de uma instância específica da classe e,
        portanto, não precisam acessar ou modificar o estado da instância (ou seja,
        os atributos de self). Como _data_hora apenas obtém e retorna a data e hora, ela não precisa usar o self.
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000_000_000, 9999_999_999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year} '
        self.cod_seguranca = f'{randint(100, 999)} {randint(100, 999)} {randint(100, 999)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)  # inserindo a propria classe (Objeto CartaoCredito) cartões na lista
        # self.conta_corrente = conta_corrente.numero #poderia adicionar somente o numero do cartao na lista

    # Método Get
    @property
    def senha(self):
        return self._senha

    # Método Set
    @senha.setter
    def senha(self, senha):
        if len(senha) > 3 and senha.isnumeric():
            self._senha = senha
        else:
            print('A nova senha não atende os requisitos de segurança.')


#Listar os atributos da instancia e seus valores
#objeto.__dict__