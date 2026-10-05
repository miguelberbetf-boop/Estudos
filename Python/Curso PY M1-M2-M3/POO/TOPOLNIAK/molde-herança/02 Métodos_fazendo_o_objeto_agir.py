'''O metodo(depositar) alterou o estado do objeto:o saldo saiu de 1 para 1'''




class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

conta = ContaBancaria('arracaeta', 1)
conta.depositar(1) #flamengo ladrão!
print(conta.saldo)