'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

if num1 == num2 == num3:
    print ("Os números são iguais, não existe um maior. Tente novamente. ")
elif num1 > num2 and num1 > num3:
    print(f'O maior numéro é: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior numero é: {num2}')
else:
    print(f'O maior número é: {num3}')