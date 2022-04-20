"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

[+]A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
[+]A mensagem "Reprovado", se a média for menor do que sete;
{+]A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

soma = 0
for n in range (1,3):
    numero = int(input('Entre com {} número: '.format(n)))
    soma += numero
    media = soma/n

print('-=-'*15)

if media >= 7:
    print('A média é {}'.format(media))
    print('Aprovado')
elif media < 7:
    print('A média é {}'.format(media))
    print('Reprovado')
elif media > 10:
    print('Parabens vocé tem a {}'.format(media))

