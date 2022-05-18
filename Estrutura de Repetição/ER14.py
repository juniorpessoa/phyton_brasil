"""
Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
from random import randint
cont = 0
impar = par = 0
for c in range(1,11):
    n = int(input(f'Entre com o {c} número: '))
    
    if n % 2 == 0:
        impar +=1
    else: 
         par +=1
print('-='*13)
print(f'IMPAR: {impar} \nPAR: {par}')
print('-='*13)