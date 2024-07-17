'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input('Em qual turno você estuda? Digte M para matutino, V para vespertino e N para noturno: ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print ('Boa Tarde!')
elif turno=='N':
    print ('Boa Noite!')
else:
    print('Caracte inválido. Tente novamente.')