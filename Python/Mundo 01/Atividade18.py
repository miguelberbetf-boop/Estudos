'''crie um programa que leia um angulo qualquer e mostre na tela o valor do seu sen. cos e tng'''
from math import cos, sin, tan
A = float(input(': '))
C = cos(A*3.14159/180)
Sen = sin(A*3.14159/180)
T = tan(A*3.14159/180)
print(f'O cos de {A} é: {C:.2f}\nO Sen de {A} é {Sen:.2f}\nA tan de {A} é {T:.2f}')