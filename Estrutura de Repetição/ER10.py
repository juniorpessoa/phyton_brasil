"""
Faça um programa que receba dois números inteiros 
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

from re import I


soma = 0
while True:
    n = int(input('Entre com um número: '))
    n2 = int(input('Entre com outro número: '))
    print('-=-'*18)
    for c in range(n,n2):
        print((c),end= ' ')
        soma += c
    print('')
    print('-=-'*18)
    print(f'\nA soma dos número : {soma}')
    break

        