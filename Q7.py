'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

idade = input("Digite sua idade: ")

if idade < '0':
    print("Idade inválida.")
elif idade > '0' and idade <='12':
    print ("Você é uma criança. ")
elif idade >'12' and idade <='18':
    print("Você é um adolescente. ")
elif idade >'18' and idade <='60':
    print ("Você é um adulto. ")
else:
    print("Você é um idoso. ")