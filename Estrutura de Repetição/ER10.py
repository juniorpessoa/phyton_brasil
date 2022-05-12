"""
Faça um programa que receba dois números inteiros 
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

while True:
    n = int(input('Entre com um número: '))
    n2 = int(input('Entre com outro número: '))

    for c in range(n,n2):
        print((c),end= ' ')
        if c < n2:
