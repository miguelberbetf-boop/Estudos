class Carrinho:
    def __init__(self, marca, modelo, ano):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        
    # métodos de instância
    def ligar(self):
        if self.ligado == False:
            self.ligado = not self.ligado  
            print(f'{self.modelo} {self.marca} ligado')
        else:
            print('2')

    def desligar(self):
        if self.ligado == True:
            self.ligado = not self.ligado  
            print(f'{self.modelo} {self.marca} desligado')
        else:
            print('1')

    def descrição(self):
        print(f'{self.marca} {self.modelo} ({self.ano})')
