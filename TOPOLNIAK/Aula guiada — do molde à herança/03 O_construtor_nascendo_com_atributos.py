class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.Saldo = saldo

conta = ContaBancaria('Trevor', 100)
print(conta.titular)
print(conta.Saldo)
