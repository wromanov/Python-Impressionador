"""
Criando nossa 1ª Classe em Python
Sempre que você quiser criar uma classe, você vai fazer:

class Nome_Classe:

Dentro da classe, você vai criar a "função" (método) __init__
Esse método é quem define o que acontece quando você cria uma instância da Classe

Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando
"""


# Criando Classe TV
class TV:

    # Atributo da classe que pode ser alterado
    fabricante = 'Sony'

    # Criando atributos de estância para classe
    # Os atributos de classe são colocados obrigatoriamente dentro de uma função init, e
    # devem possuir o "self" para serem acessados.
    def __init__(self, cor, volume):
        self.cor = cor
        self.ligada = False
        self.tamanho = 60
        self.canal = 10
        self.volume = int(volume)

    # Criando métodos para classe
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


# Instanciando TV
tv_sala = TV('laranja', 35)
tv_quarto = TV('roxo', 40)

# Altera o canal da TV
tv_quarto.mudar_canal('disnei')
tv_sala.mudar_canal('hbo')


# Alterando atributo da TV
tv_quarto.tamanho = 55
tv_sala.tamanho = 50

# Alterando atributo da Classe
TV.fabricante = 'MTI'


print(tv_quarto.tamanho)
print(tv_quarto.volume)
print(tv_quarto.cor)

print(tv_sala.tamanho)
print(tv_sala.volume)
print(tv_sala.cor)

print(tv_sala.fabricante)
print(tv_quarto.fabricante)
