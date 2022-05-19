"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

print('-='*20)
menor = maior = 0
cont = 0

escolha = int(input('Entre com a quantidade de número desejado: '))
print(escolha)
for c in range(1,escolha+1):
    n = int(input(f'Entre com o {c} número: '))
    if menor >= 0:
        menor = n
    else:
       menor = n

print(menor)
