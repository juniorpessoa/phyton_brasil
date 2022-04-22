"""
Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar
 M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor
"""
print('QUAL SEU PERÍODO ESCOLAR')
print()
print('Periodo Escolar \n[M] - MATUTINO \n[V] - VERPERTINO \n[N] - NOTURNO:')

periodo = str(input('ENTRE COM O SEU PERÍODO:').upper().strip())

if periodo == 'M':
    print('BOM DIA')
elif periodo == 'V':
    print('BOA TARDE')
elif periodo == 'N':
    print('BOA NOITE')
else:
    print('Entre com o valor valido ')