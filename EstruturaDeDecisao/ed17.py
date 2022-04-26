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
print('  METRAGEM DE ÁREA DESEJADA : {}m²'.format(area))
print('-=-'*12)

print('VERIFICAÇÃO ...')
sleep(3)
medidagalao = area/3




print('-=-'*12)
print('QUANTIDADE DE TITA A SER UTILIZADA:')
#arredondando as latas usadas
medidagalao = math.ceil(medidagalao)
print('LITROS UTILIZADOS {}L'.format(medidagalao))
print('-=-'*12)
print('')
#galão de 18 litros
dezoito = medidagalao/18
lt_dezoito = math.ceil(dezoito)
vl_dezoito = lt_dezoito * 80

print('[+]COMPRAR APENAS LATAS DE 18 LITROS: \nQtd.: {} ------------------- R$:{:.2f}'.format(lt_dezoito,vl_dezoito))


print()
print('-=-'*12)
print()
#galão de 3.6 litros
treseseis = medidagalao/3.6
lt_treseseis = math.ceil(treseseis)
vl_treseseis = lt_treseseis * 25



print('[+]COMPRAR APENAS GALÃO DE 3.6 LITROS: \nQtd.: {} ------------------- R$:{:.2f}'.format(lt_treseseis,vl_treseseis))
print()
print('-=-'*12)
print('[+]MISTURANDO AS LATAS E GALÕES: ')
int_dezoito = math.trunc(dezoito)
vl_dezoito = dezoito * 80
print('        [+]COMPRAR APENAS LATAS DE 18 LITROS: \nQtd.: {:.2f} '.format(dezoito))

    #print('   [+]LATAS DE 18l: \n      x Qtd.: ------------------ R$ xx,xx\n')
    #print('   [+]LATAS DE 3.6l: \n      x Qtd.: ------------------ R$ xx,xx\n')
    #print('   [+]TOTAL:         \n      x Qtd.: ------------------ R$ xx,xx\n')

#VERIFICAR E ARRUMAR O EXERCICIOS TEM PENDENCIAS