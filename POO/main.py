import ContasBancos

conta_walace = ContasBancos.ContaCorrente('Walace', 14088713788, 3321, 30405, 34)
cartao_walace = ContasBancos.CartaoCredito('Walace', conta_walace)

conta_walace.depositar(5000)

print(conta_walace.consultar_saldo())

