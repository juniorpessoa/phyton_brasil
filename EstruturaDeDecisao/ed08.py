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
elif valor1 > valor3 < valor2:
    print('Produto mais barato R$: {:.2f}'.format(valor3))
# se alguns números forem iguais
elif valor1 == valor2 and valor1 and valor2 < valor3:
    print('Produtodo {} e {} são menores.'.format(valor1,valor2))
elif valor1 == valor3 and valor1 and valor3 < valor2:
    print('Produtodo {} e {} são menores.'.format(valor1,valor3))
elif valor2 == valor3 and valor2 and valor3 < valor1:
    print('Produto {} e {} são menores'.format(valor2,valor3))
else:
    print('todos são iguais')