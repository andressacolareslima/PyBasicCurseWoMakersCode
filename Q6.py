'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente 
utilizando somente letras maiúsculas.
Dica:lembrese que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''


seu_nome = input("Digite seu nome: ")

seu_nome_str = seu_nome.split()

lista_maiusculo =[s.upper()[::-1] for s in seu_nome_str]

nomes_invertidos = ' '.join (lista_maiusculo)

print(nomes_invertidos)