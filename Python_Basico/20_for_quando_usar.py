"""
Quando usar o "For item in lista"  ou "For i in range"
"""
produtos = ["iphone", "ipad", "airpod", "macbook"]
precos = [7000, 10000, 2500, 14000]

# For item in lista - Usamos quando temos apenas uma lista a percorrer.
for preco in precos:
    print(preco * 1.2)
print()

# For i in range / For Inumerate - Usamos quanto temos mais de uma lista a percorrer, e precisamos do índice.
for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto, preco)
 