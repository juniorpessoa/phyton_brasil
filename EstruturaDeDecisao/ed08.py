"""
Faça um Programa que leia três números e mostre o maior e o menor deles
"""

print('Merceria COMPRE BEM')
print('-=-'*15)
print('ENTRE COM OS SEUS PRODUTOS \nE OS VALORES')
print('-=-'*15)
valor1 = int (input('Entre com o valor: R$:'))
valor2 = int (input('Entre com o valor: R$:'))
valor3 = int (input('Entre com o valor: R$:'))

if valor2 > valor1 < valor3:
    print('Produto mais barato R$:{:.2f}'.format(valor1))
elif valor1 > valor2 < valor3:
    print('Produto mais barato R$: {:.2f}'.format(valor2))
else:
    print('Produto mais barato R$: {:.2f}'.format(valor3))