"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

n= 0
while 0 >= n <=10:
    n = int(input('Entre com número válido: '))
print('fim')