# Formas de interromper um for

### 2 Opções:

# - break -> interrompe e finaliza o for
# - continue -> interrompe e vai para o próximo item do for

vendas = [100, 150, 1500, 2000, 120]

meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break
    print(venda)

vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']

meta2 = 130

for venda in vendas:
    if venda < meta2:
        continue
    print(venda)