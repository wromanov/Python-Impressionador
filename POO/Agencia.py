from symtable import Class


class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = []
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa Atual R$ {self.caixa}')
        else:
            print(f'O valor de Caixa está Ok. Caixa Atual R$ {self.caixa}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print(f'Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# Conceito de Herança
# Criando uma subclasse, a qual herda os atributos e métodos da classe pai (super classe).
# A classe pai é passada como argumento para a subclasse em seu construtor.

class AgenciaVirtual(Agencia):

    # alterando o construtor da Agencia Virtual, para solicitar o site da agencia virtual
    def __init__(self, site, telefone, cnpj, numero):
        self.site = site

        # chamado o construtor da classe pai, e passando os valores para os atributos.
        super().__init__(telefone, cnpj, numero)

        # Definindo o valor de caixa da Agencia virtual
        self.caixa = 2000000


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass


agencia1 = Agencia(21996932687, 223075068, 4568)
agencia1.caixa = 1_000_000
agencia1.verificar_caixa()

agencia_virtual = AgenciaVirtual('meubancovirtual.com', 37555215, 123456789, 3321)
agencia_virtual.verificar_caixa()
