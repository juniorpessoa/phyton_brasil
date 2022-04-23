"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

"""
print('Veificando o dia da semana:')
print("""
1 - DOMINGO
2 - SEGUNDA-FEIRA
3 - TERÇA-FEIRA
4 - QUARTA-FEIRA
5 - QUINTA-FEIRA
6 - SEXTA-FEIRA
7 - SABADO
""")

opção = int(input('Entre com a Opção desejada: '))

if opção == 1:
    print('Domingo')
elif opção == 2:
    print('Segunda - Feira')
elif opção == 3:
    print('Terça - Feira')
elif opção == 4:
    print('Quarta - Feira')
elif opção == 5:
    print('Quinta - Feira')
elif opção == 6:
    print('Sexta - Feira')
elif opção == 7:
    print('SABADO')
else:
    print('Por favor entrar com opção válida')