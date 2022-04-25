"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""
import math

print('Escola do Guana-Bara')

soma = 0
for notas in range(1,3):
    n = int(input('Entre com o {} valor: '.format(notas)))
    soma += n
media = soma/notas

if media >= 9 and media ==10:
    print('{}A'.format(media))
elif media <= 9 and media >= 7.5:
    print('{}B'.format(media))
elif media <= 7.5 and media >= 6:
    print('{}C'.format(media))
elif media <= 6 and media >= 4:
    print('{}C'.format(media))
elif media <= 4 and media >= 0:
    print('{}D'.format(media))
else:
    print('ENTRE COM VALORES CORRETOS')