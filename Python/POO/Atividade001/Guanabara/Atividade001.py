#declaração de Classes
class Gafanhoto:
    def __init__(Self):#metodo construtor


    # Atributos de instancia
        Self.nome = ""
        Self.idade = 0
        Self.punheta = 0
    #Metodos de instancia
    def aniversario(self):
        self.idade = self.idade +1 #ou pode ser substituido por +=

    def masturbar(self):
        self.punheta = self.punheta +1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade e bateu {self.punheta} punhetas hoje.'


    

#Declaração de objeto
G1 = Gafanhoto()            #Observação: quand não tem parentese é um atributo
G1.nome = "Miguel"          #quando tem parenteses é um método     
G1.idade = 15
G1.masturbar()
print(G1.mensagem())


g2 = Gafanhoto()
g2.nome = 'Maylon'
g2.idade = 15
g2.aniversario()
print(g2.mensagem())


g3 = Gafanhoto()
g3.nome = 'Thaison'
print(g3.mensagem())