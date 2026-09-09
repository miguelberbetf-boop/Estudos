'''crie um progrma que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.'''
'''n = float(input(''))
print(f'A porção inteira de {n} é {n:.0f}')'''



'''ou'''


'''n = float(input(''))
print(f'A porção inteira de {n} é {int(n)}')'''


'''ou'''
from math import trunc
while True:

    n = float(input(''))
    print(f'A porção inteira de {n} é {trunc(n)}')
    if n == 0:
        print('Programa encerrado')
        break