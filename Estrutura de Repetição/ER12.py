""""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
"""
cont = 0
n = int (input('ENTRE COM UMA TABUDA: '))
print('')
for c in range (0,11):
    print(f'{n} x {cont} = {n*cont}')
    cont += 1