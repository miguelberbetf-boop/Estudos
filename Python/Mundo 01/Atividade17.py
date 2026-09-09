'''faça um programa que leia o cateto oposto e o cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''
Cad = float(input(''))
Cop = float(input(''))
H = (Cad**2)+(Cop**2)
print(f'A Hipotenusa vale: {H**0.5:.1f}')


'''ou'''

from math import hypot
c1 = float(input(''))
c2 = float(input(''))
H = hypot(c1, c2)
print(f'{H}')