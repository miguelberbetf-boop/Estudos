class ContaBancaria:
    banco = "baconzitos bank"
    tc = 0


    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.Saldo = saldo


    def sacar(self, valor):
        if valor <= self.Saldo:
            self.Saldo -= valor
        else:
            print('Saldo insuficiente!')

    def ver_saldo(self):
        print(f'[{self.banco}] {self.titular}: R$ {self.Saldo:.2f}')


conta1 = ContaBancaria('Trevor', 1000)     #conta é um OBJETO(instância criado a partir do molde .titular)
conta2 = ContaBancaria('Guanabara', 10000)
print(conta2.titular)
print(conta2.Saldo)
conta2.ver_saldo()

print('='*32)

print(conta1.titular)
print(conta1.Saldo)
conta1.ver_saldo()


class Poupanca(ContaBancaria):
    def render_juros(self, taxa):
        self.Saldo += self.Saldo *taxa

print('-'*32)
Poupanca = Poupanca('JUBISCLEVALDO', 67000)
Poupanca.render_juros(0.10)

print('-'*32)
Poupanca.ver_saldo()