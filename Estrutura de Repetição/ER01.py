nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while len(nome)<=3:
  nome = input('Nome: (com mais de 3 letras)')

while idade < 0 or idade > 150 :
  idade = input('Idade:(entre 0 e 150) ')

while salario <= 0:
  salario = input('Salário: (maior que 0) ')

