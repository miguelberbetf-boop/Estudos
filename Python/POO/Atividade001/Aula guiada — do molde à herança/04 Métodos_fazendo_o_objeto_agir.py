'''O obe'''



class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.Saldo = saldo


    def sacar(self, valor):
        if valor <= self.Saldo:
            self.Saldo -= valor
        else:
            print('Saldo insuficiente!')


conta = ContaBancaria('Trevor', 1000)     #conta é um OBJETO(instância criado a partir do molde .titular)
print(conta.titular)
conta.sacar(10000)
print(conta.Saldo)

