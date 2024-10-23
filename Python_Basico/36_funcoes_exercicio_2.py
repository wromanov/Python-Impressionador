# Calcular Carga Tributária de um Produto

def calcular_tributo(preco, custo, lucro):
    imposto = preco - custo - lucro
    carga = imposto / preco
    return carga


print(calcular_tributo(1500, 400, 800))