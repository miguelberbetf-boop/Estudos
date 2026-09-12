class Gafanhoto:
    '''
essa classe cria um gafanhoto com nomee idade

para criar um novo gafanhoto use: vriavel = Gafanhoto(nome, idade)
    '''
    def __init__(Self, n = '', i = 0):#metodo construtor

    # Atributos de instancia
        Self.nome = n
        Self.idade = i
    #Metodos de instancia
    def aniversario(self):
        self.idade = self.idade +1 #ou pode ser substituido por +=


    def __str__(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade .'


    def __getstate__(self):
        return f'estate: {self.nome}' 


    #Declaração de objeto
g1 = Gafanhoto('Miguel', 15)            #Observação: quand não tem parentese é um atributo
print(g1)

g2 = Gafanhoto('MArcio', 64)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3)


print('='*32)
print(g1.__doc__)
print('='*32)
print(g1.__dict__)
#ou
print(g1.__getstate__())

print(g1.__class__)