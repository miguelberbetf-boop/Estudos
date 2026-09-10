

class Aluno:
    def __init__(self, aluno, idade, curso, nota):
        self.aluno = aluno
        self.idade = idade
        self.curso = curso
        self.nota = nota


    def mostrar_dados(self):
        print(f'Nome:{self.aluno} | Idade: {self.idade} | Curso: {self.curso} | Nota: {self.nota:.1f}')


    def alterar_nota_notanova(self, nota):
        self.nota = int(input(f"Alterar nota de {self.aluno}: "))



        '''self.nota = nota
        print'''


    def situacao(self):
        if self.nota >= 60:
            print(f"O aluno {self.aluno} está Aprovado")
        else:
            print(f"O aluno {self.aluno} Reprovado")

Jeferson = Aluno('Jeferson', 10, 'TI', 60)
Jeferson.alterar_nota_notanova(100)
Jeferson.mostrar_dados()
Jeferson.situacao()