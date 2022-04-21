"""
Faça um Programa que leia
três números e mostre o maior deles.
"""

n1 = int(input('Entre com o 1° número: '))
n2 = int(input('Entre com o 2° número: '))
n3 = int(input('Entre com o 3° número: '))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


print('O maior número é {}'.format(maior))
