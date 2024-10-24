import numpy as np

# Criando objeto gerador de números
rng = np.random.default_rng()  # Objeto gerador

# Gerando um número aleatório
numero = rng.random()  # por padrão gera numero entre 0 e 1
numero2 = rng.random() * 10  # Multiplicando o valor por 10 vai gerar números entre 0 e 10

# Fixando os números gerados para que não mudem ao executar o código
rng = np.random.default_rng(seed=0)

# Gerando um array com 10 números entre 0 e 100
array = rng.random(30) * 100

# Gere dados de vendas falsos para 30 dias
# Vamos supor que as vendas de um produto podem variar de 50 a 200 por dia
dados_vendas = rng.integers(low=50, high=200, size=30)

print(numero)
print(numero2)
print(array)
print(dados_vendas)

"""
Agora, você pode usar esses dados para realizar várias análises. Por exemplo, 
você pode querer saber qual foi o dia com as vendas mais altas, as vendas mais baixas, 
ou a média de vendas durante o mês. Aqui está como você pode fazer isso:
"""
# Maior venda do mês
maior_venda = array.max()

# Menor venda do mês
menor_venda = array.min()

# Dia do mês com a maior venda / argmax informa o índice o item na lista de maior valor.
dia_maior_venda = array.argmax()

# Dia do mês com a menor venda / argmin informa o índice o item na lista de menor valor.
dia_menor_venda = array.argmin()

# Media de vendas
media_vendas = np.mean(array)


print(f'A maior venda do mês foi de R$ {maior_venda:.2f} no dia {dia_maior_venda + 1}.')
print(f'A menor venda do mês foi de R$ {menor_venda:.2f} no dia {dia_menor_venda + 1}.')
print(f'Media de vendas do mês foi de R$ {media_vendas:.2f}.')

print(np.median(dados_vendas))

print(np.percentile(dados_vendas, 50))

print(np.std(dados_vendas))

print(np.var(dados_vendas))

"""
Breve resumo e conceitos simplificados das funções estatísticas citadas:

1. Mediana:
A mediana é um valor que divide um conjunto de dados em duas partes iguais. Para encontrá-la, você deve organizar os dados em ordem crescente ou decrescente e escolher o valor do meio. Se houver um número ímpar de dados, a mediana será exatamente o valor central. Se houver um número par de dados, a mediana será a média dos dois valores do meio.

2. Percentil:
O percentil é uma medida estatística que indica a posição relativa de um dado dentro de um conjunto de dados. Ele informa a porcentagem de valores que estão abaixo desse dado. Por exemplo, o percentil 50 (também conhecido como mediana) divide os dados em duas partes iguais, com 50% dos valores abaixo dele e 50% acima.

3. Desvio padrão:
O desvio padrão é uma medida que indica o quão dispersos os valores de um conjunto de dados estão em relação à média. Ele mostra a variabilidade dos dados em relação ao valor médio. Um desvio padrão maior indica que os dados estão mais espalhados, enquanto um desvio padrão menor indica que os dados estão mais próximos da média.

4. Variância:
A variância é outra medida de dispersão que indica o quão distantes os valores de um conjunto de dados estão da média. Ela é calculada como a média dos quadrados das diferenças entre cada valor e a média. A variância fornece uma medida da dispersão total dos dados, independentemente de serem maiores ou menores que a média.

"""