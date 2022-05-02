"""
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
 que calcule e escreva o número de anos necessários para que a população
 do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

print('HABITANTES GLOBAIS')
print('-=-'*15)
A = int(input('ENTRE COM A POPULAÇÃO DE A:'))
taxaA = int(input('ENTRE COM A TAXA POPULACIONAL DE A: '))
taxaA /= 100
B = int(input('ENTRE COM A POPULAÇÃO DE B:'))
taxaB = int(input('ENTRE COM A TAXA POPULACIONAL DE B: '))
taxaB /= 100
#QUAL ANO SERÁ IGUALADO OU MAIOR QUE A DO MAIS B
ano = 0
while A > B:
    A *= taxaA
    B *= taxaB
    ano += 1
print(ano)

