'''Um objeto não serve só para guardar dados; ele também faz coisas. Essas ações são os métodos.'''






class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.Saldo = saldo

conta = ContaBancaria('Trevor', 100)     #conta é um OBJETO(instância criado a partir do molde .titular)
print(conta.titular)
print(conta.Saldo)



