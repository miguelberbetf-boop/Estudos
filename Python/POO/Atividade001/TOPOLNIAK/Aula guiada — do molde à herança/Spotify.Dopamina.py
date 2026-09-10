import time

class spotify:
    def __init__(self, titulo, artista, duracao, curtidas):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.duracao = curtidas
        self.curtida = 0


    def tocar(self):

        while self.duracao >= 0:
            print(f'{self.duracao:.2f}')

            self.duracao -= 0.01

            self.duracao = round(self.duracao, 2)

            time.sleep(1)


    def curtir(self):
        self.curtidas +=1
       


    def descurtir(self):
        if self.titulo == 0:
            print('não há curtida nessa musica')
        else:
            self.curtida -=1
            print('musica descurtida')


    def mostrar(self):
        print(f'{self.titulo} {self.artista} {self.duracao} {self.curtidas}')



Wellcome_to_the_family = spotify('Wellcome_to_the_family', 'Avenged sevenfold', 12800000, 4.05, )
Wellcome_to_the_family.tocar()