'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''

lado1 = input('Digite primeiro comprimento do triângulo: ')
lado2 = input('Digite o segundo comprimento do triângulo: ')
lado3 = input('Digite o terceiro comprimento do triângulo: ')

if lado1 == lado2 ==lado3:
    print("Esse triângulo é um triângulo do tipo equilátero. ")
elif lado1 == lado2 or lado2==lado3 or lado3==lado1:
    print("Esse triângulo é um triângulo do tipo isósceles.")
else:
    print("Esse triângulo é um triângulo do tipo escaleno.")