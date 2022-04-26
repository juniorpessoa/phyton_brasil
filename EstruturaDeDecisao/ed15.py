"""
Faça um Programa que peça os 3 lados de um triângulo.
 O programa deverá informar se os valores podem ser um triângulo.

Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
print('Entre com os 03 lado de um triangulo:')
l1 = int(input('Entre com o primerio lado: '))
l2 = int(input('Entre com o segundo lado: '))
l3 = int(input('Entre com o terceiro lado: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2 :
    print('Forma um triangulo')
    if l1 == l2 == l3 == l1:
        print('Triangulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triangulo Isóceles: Todos angulos Iguais')
    else:
        print('Triangulo Isóceles')
else:
    print('Não forma um Triangulo')