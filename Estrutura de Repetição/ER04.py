"""
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
 que calcule e escreva o número de anos necessários para que a população 
 do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

print('HABITANTES GLOBAIS')
print('-=-'*15)
print('PAIS A: POPULAÇÃO 80000\n[+]TAXA ANUAL DE CRESCIMENTO DE  3%')
print('-=-'*15)
print('PAIS B: POPULAÇÃO 200000\n[+]TAXA ANUAL DE CRESCIMENTO DE  1.5%')

#QUAL ANO SERÁ IGUALADO OU MAIOR QUE A DO MAIS B

A = 80000
B = 200000

taxaA = 0.03
taxaB = 0.015
ano = 0


while A < B:
    A += (A * taxaA)
    B += (B * taxaB)
    ano += 1
print(ano)