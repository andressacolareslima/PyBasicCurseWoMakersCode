'''Faça um Programa que peça dois números e imprima o maior deles'''
n1 = input('Digite um número: ')
n2 = input ('Agora, digite outro número: ')

if n1>n2:
    print(f'O maior número é {n1}')
elif n1==n2:
    print('Os números são iguais. Tente novamente. ')
else:
    print(f'O maior número é {n2}')