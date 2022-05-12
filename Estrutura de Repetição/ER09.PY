"""
Faça um programa que imprima na tela apenas os 
números ímpares entre 1 e 50.
"""
from pprint import pprint
from string import printable


cont = 0
for c in range(1,51,2):
    print((c),end=' ')
    
    cont += 1
print((f'\nExistem {cont} nessa contagem').upper())
