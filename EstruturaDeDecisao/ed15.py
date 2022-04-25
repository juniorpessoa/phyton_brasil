"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

print('Entre com os dados para verificação do TRIANGULO')

l1 = int(input('Entre com primeiro lado: '))
l2 = int(input('Entre com segundo lado: '))
l3 = int(input('Entre com o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l2 and l3 < l1 + l2:
    print('FORMA UM TRIANGULO')
    if l1 == l2 == l3:
        print('Triângulo Equilátero: Possui os lados iguais')
    elif l1 == l2 or l1 == l3 or l2 ==l3:
        print('Triangulo Isóceles: Quaisquer dois lados iguais')
    else:
        print('Triângulo Escaleno')
else:
    print('NÃO FORMA UM TRIANGULO')