"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
from time import sleep

print('==== VALIDANDO OS DADOS ===')
sleep(2)
nome = str(input('Entre com o seu nome: '))
while len(nome) <= 3:
    nome = str(input('ENTRE NOVAMENTE COM OUTROS LOGUIN: ').strip().upper())

idade = int(input('Entre com a sua idade: '))
while idade <= 0 or idade >= 150:
    idade = int(input('ENTRE COM A SUA IDADE: '))

salario = int(input('Seu salário: '))
while salario <= 0:
    salario = int(input('ENTRE NOVAMENTE COM O SEU SALÁRIO: R$:'))

sexo = str(input('Entre com seu sexo: [F] - FEMININO / [M] - MASCULINO: '))
while sexo != "F" and sexo != 'M':
    print('ATENÇÃO, end'')
    sexo = str(input('Entre com seu sexo: [F] - FEMININO / [M] - MASCULINO: ')).upper())

estado_civil = str(input("""Faça um programa que leia e valide as seguintes informações:
Estado Civil: \n[S] - SOLTEIRO\n[C] - CASADO \n[V] - VIUVO\n[D] - DIVORCIADO\nEntre com a opção desejada: """))
print('Escolha Civi:')

while estado_civil != "S" and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    input("""Faça um programa que leia e valide as seguintes informações:
    Estado Civil: \n[S] - SOLTEIRO\n[C] - CASADO \n[V] - VIUVO\n[D] - DIVORCIADO\nEntre com a opção desejada: """)

