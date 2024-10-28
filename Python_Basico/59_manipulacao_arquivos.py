"""
Open 'W' = Abertura do Arquivo em Modo Escrita (Sobre escreve o que já foi escrito)
Open 'W' = Abertura do Arquivo em Modo Apend (Adiciona na mesma linha o que foi escrito)

"""
from matplotlib.textpath import text_to_path

# # Abrindo o arquivo
# arquivo = open('nomes_dados.txt', 'a')
# # arquivo.write('Walace 34\n')  # Escreve no arquivo
# condicao = ''
#
# while True:
#     arquivo.write(input('Digite nome e idade: ') + '\n')  # Escreve no arquivo
#     condicao = input('Deseja sair [s] / [n]').casefold().strip()
#     if condicao == 's':
#         break

# Nomeia uma função de abertura, quando o programa sai do escopo o arquivo é fechado.
with open('nomes_dados.txt', 'r') as arquivo:

    resultados = arquivo.readlines()  # Faz a leitura de cada linha do arquivo.

    # print(resultados)

    lista_nomes = []

    # Insere nome e idade numa lista
    for nomes in resultados:
        lista_nomes.append(nomes.split())

    print([nomes for nomes in lista_nomes])
