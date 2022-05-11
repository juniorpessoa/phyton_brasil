"""
Faça um programa que leia 5 números e informe o maior número.
"""
notas = media = maior = 0
for n in range(1,6):
   n = int(input('Entre com um número: '))

   if n > maior:
      maior = n

   notas += n
   media = notas/n
 
print(media)
print(maior)

