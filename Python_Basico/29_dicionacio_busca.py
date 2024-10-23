# Não confie na ordem dos dicionários, use as chaves

### Python Versões Antigas x Versões Novas

# - Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves
# - 2 formas de pegar um valor:
# - dicionario[chave]
# - .get(chave)

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu',
                 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000,
                     'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500,
                     'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

### Verificar se item está no dicionário:

# - if
# - .get(chave) = None
# Se tentarmos procurar as vendas de "copo" na lista de vendas tecnologia, o que acontece?

# Método Get

if vendas_tecnologia.get('copo') is None:
    print('Copo não está dentro da lista de produtos de tecnologia.')
else:
    print(vendas_tecnologia.get('copo'))

# Método índice

if 'copo' in vendas_tecnologia:
    print(print(vendas_tecnologia['copo']))
else:
    print('Copo não está dentro da lista de produtos de tecnologia.')
