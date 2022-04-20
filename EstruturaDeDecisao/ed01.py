"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

print('Entre com dois número')
print('-=-'*15)

n1 = int(input('Entre com o primeiro número:'))
n2 = int (input('Entre com o segundo número:'))
print('-=-'*15)
if n1 > n2:
    print('O primeiro número {} \né maior que o segundo {}'.format(n1,n2))
else:
    print('O segundo número {} \né maior que o primeiro {} '.format(n2,n1))