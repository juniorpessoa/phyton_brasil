"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = str(input('Digite (F)-Feminino , (M)-Masculino: ').strip().upper())

if sexo == 'M':
    print('Sexo Masculino:')
if sexo == 'F':
    print('Sexo Feminino:')
else:
    print('Atenção: Digite novamente ...')
    sexo = str(input('Digite (F)-Feminino , (M)-Masculino: ').strip().upper())



