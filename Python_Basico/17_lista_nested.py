# Lista dentro de lista

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

"""
- Quanto João vendeu de IPad?
- Quanto Diego vendeu de IPhone
- Qual o total de vendas de IPhone?
"""

vendas_joao_ipad = vendas[1][0]
vendas_joao_iphone = vendas[1][1]

print(vendas_joao_ipad)
print(vendas_joao_iphone)

print(vendas[0])
