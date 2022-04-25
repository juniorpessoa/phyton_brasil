"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

print("""MENU

[1] - DOMINGO
[2] - SEGUNDA - FEIRA
[3] - TERÇA - FEIRA
[4] - QUARTA - FEIRA
[5] - QUINTA - FEIRA
[6] - SEXTA - FEIRA
[7] - SABADO""")
print('')
dia = int (input('Entre com o dia da SEMANA:'))


if dia == 1:
     print('DOMINGO')
elif dia == 2:
    print('SEGUNDA - FEIRA')
elif dia == 3:
    print('TERÇA - FEIRA')
elif dia == 4:
    print('QUARTA - FEIRA')
elif dia == 5:
    print('QUINTA - FEIRA')
elif dia == 6:
    print('SEXTA - FEIRA')
elif dia == 7:
    print('SABADO')
else:
    print('ENTRE COM ALGUM VALOR VALIDO DE 1 A 7')
    
print('Fianlizando')