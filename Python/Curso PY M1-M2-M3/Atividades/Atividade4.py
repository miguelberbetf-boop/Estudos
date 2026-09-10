#Exercício 4: Dissecando uma Variável
Frase = input('digite algo: ')
print(f'essa frase tem {len(Frase)} caracter')
print(f'Só tem espaços? {Frase.isspace()}')
print(f'Está toda maisuscula? {Frase.isupper()}')
print(f'É decimal? {Frase.isdecimal()}')
print(f'Essa frase está minuscula? {Frase.islower()}')