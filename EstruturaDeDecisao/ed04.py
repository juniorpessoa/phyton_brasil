"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
n = str(input('ENTRE COM UMA LETRA: ').upper().strip())
print('-=-'*15)

if n.isalpha():
    if n == "A":
        print('VOGAL')
    if n == "E":
        print('VOGAL') 
    if n == "I":
        print('VOGAL')
    if n == "O":
        print('VOGAL')
    if n == "U":
        print('VOGAL')
    else:
        print('CONSOANTE')