"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
from time import sleep
print('CRIANDO LOGUIN E SENHA')
print('')
login  = str(input('ENTRE COM O LOGUIN E SENHA: '))
senha = str(input('ENTRE COM UM LOGUIN: '))

while login == senha:
    sleep(2)
    print('-=-'*22)
    print('LOGUIN E SENHA IGUAIS ....')

    sleep(2)
    print('ENTRE COM NOVAS CREDENCIAIS...')
    print('-=-' * 22)
    login = str(input('ENTRE COM O LOGUIN E SENHA: '))
    senha = str(input('ENTRE COM UM LOGUIN: '))
print('ENTRAMOS NO SISTEMA')