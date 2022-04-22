"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
 que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,

dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
from time import sleep
import  math
print('')
print('FOLHA DE PAGAMENTO')
sleep(2)
print('CALCULANDO SEU SALÁRIO')
sleep(2)
print('-=-'*12)
sleep(2)
print('PROCESSANDO')
sleep(2)
print('-=-'*12)
sleep(3)
salario = float(input('Entre com o seu salário bruto: ').strip())
sleep(2)
print('-=-'*13)
print('Atualizando...')
print('-=-'*13)
print('Salário Atual              R$:  {:.2f}'.format(salario))

if salario <= 900:
    inss = salario * 0.10
    desconto = 0
    print('ISENTO                     R$:    {:.2f}'.format(desconto))
    print('(-)INSS (10%)              R$:   {:.2f}'.format(inss))
    descontos = desconto + inss
    print('Total de Desconto          R$:   {:.2f}'.format(descontos))
    liquido = salario - descontos
    fgts = salario * 0.11
    print('---'*13)
    print('FGTS - (11%)               R$:   {:.2f}'.format(fgts))
    print('PAGO PELA EMPRESA')
    print('---'*13)
    print('Salario Liquido:           R$:  {:.2f}'.format(liquido))
elif salario >= 900 and salario <= 1500:
    inss = salario * 0.10
    desconto = salario * 0.05
    print('(-)IR 5%                   R$:    {:.2f}'.format(desconto))
    print('(-)INSS (10%)              R$:   {:.2f}'.format(inss))
    descontos = desconto + inss
    print('Total de Desconto          R$:   {:.2f}'.format(descontos))
    liquido = salario - descontos
    print('---'*13)
    fgts = salario * 0.11
    print('FGTS - (11%)               R$:   {:.2f}'.format(fgts))
    print('PAGO PELA EMPRESA')
    print('---'*13)
    print('Salario Liquido:           R$:  {:.2f}'.format(liquido))
elif salario >= 1500 and salario <= 2500:
    inss = salario * 0.05
    desconto = salario * 0.10
    print('(-)IR 10%                  R$:   {:.2f}'.format(desconto))
    print('(-)INSS (10%)              R$:   {:.2f}'.format(inss))
    descontos = desconto + inss
    print('Total de Desconto          R$:   {:.2f}'.format(descontos))
    liquido = salario - descontos
    print('---'*13)
    fgts = salario * 0.11
    print('FGTS - (11%)               R$:   {:.2f}'.format(fgts))
    print('PAGO PELA EMPRESA')
    print('---'*13)
    print('Salario Liquido:           R$:  {:.2f}'.format(liquido))
else:
    inss = salario * 0.05
    desconto = salario * 0.20
    print('(-)IR 5%                   R$:  {:.2f}'.format(desconto))
    print('(-)INSS (20%)              R$:   {:.2f}'.format(inss))
    descontos = desconto + inss
    print('Total de Desconto          R$:   {:.2f}'.format(descontos))
    liquido = salario - descontos
    print('---'*13)
    fgts = salario * 0.11
    print('FGTS - (11%)               R$:   {:.2f}'.format(fgts))
    print('PAGO PELA EMPRESA')
    print('---'*13)
    print('Salario Liquido:           R$:  {:.2f}'.format(liquido))


