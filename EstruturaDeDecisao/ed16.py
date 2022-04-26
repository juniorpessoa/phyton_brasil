"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math
from time import sleep

print('TINTAS JARBAS')
print('')
lado = int(input('QUAL LARGURA: '))
altura = int(input('QUAL ALTURA: '))
area = lado * altura
print('-=-'*12)
print('''COBERTURA DE TINTA É DE 1 LITRO 
PARA CADA 3 M²''')
print('-=-'*12)
print('Metragem da área desejada : {}m²'.format(area))
print('-=-'*12)

print('VERIFICAÇÃO ...')
sleep(3)
medidagalao = area/3
print('-=-'*12)

if medidagalao > 18:
       galao = medidagalao /18
       print('Galão necessário: {:.2f}'.format(galao))
       pagar = galao * 80
       print('Valor a ser pago R$: {:.2f}'.format(pagar))
else:
    galao = 1
    print('Galão necessário: {}'.format(galao))
    pagar = galao * 80
    print('Valor a ser pago R$: {:.2f}'.format(pagar))
