class Banco:
    ''' 
permite criar uma conta bancaria
    '''
    def __init__(self, id, nome, saldo =0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f'A conta número: {self.id},  de {self.nome} possui saldo de: R${self.saldo:,.2f}'


    def deposito(self, valor):
        self.saldo += valor
        return f'Deposito de {valor:,.2f} autorizado!'


    def sacar(self, valor):
        if valor > self.saldo:
            return 'Saldo insuficiente!'
        else:
            self.saldo -= valor
            return f'Saque de {valor:,.2f} autorizado.'






c1 = Banco(805, 'Miguel', 100)
c1.deposito(50000000000000)
c1.sacar(5000000000000)
print(c1)
