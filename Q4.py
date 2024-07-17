'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
e calcule quanto poderia comprar de cada moeda estrangeira. 

Considere a tabela de conversão abaixo:
Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suíço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21 '''

def converter_p_dolar (moeda_real, dolar_us):
    convertido = moeda_real / dolar_us
    return convertido

def converter_p_peso (moeda_real, peso_arg):
    convertido = moeda_real / peso_arg
    return convertido

def converter_p_dolar_aus(moeda_real, dolar_aus):
    convertido = moeda_real / dolar_aus
    return convertido

def converter_p_dolar_can(moeda_real, dolar_can):
    convertido = moeda_real / dolar_can
    return convertido

def converter_p_franco (moeda_real, franco_su):
    convertido = moeda_real / franco_su
    return convertido

def converter_p_euro (moeda_real, euro):
    convertido = moeda_real / euro
    return convertido

def converter_p_libra_uk(moeda_real, libra_uk):
    convertido = moeda_real / libra_uk
    return convertido

moeda_real = float(input("Digite o valor da sua carteira em Reais: "))
dolar_us = 4.91
peso_arg = 0.02
dolar_aus = 3.18
dolar_can = 3.64
franco_su = 0.42
euro = 5.36
libra_uk = 6.21

dolar_americano = converter_p_dolar(moeda_real, dolar_us)
peso_argentino = converter_p_peso(moeda_real, peso_arg)
dolar_australiano = converter_p_dolar_aus (moeda_real, dolar_aus)
dolar_canadense = converter_p_dolar_can (moeda_real, dolar_can)
franco_suico = converter_p_franco (moeda_real, franco_su)
euro_europeu = converter_p_euro (moeda_real, euro)
libra_esterlina = converter_p_libra_uk (moeda_real, libra_uk)

print (f'\nSe você tem R${moeda_real}:\nEm dólar americano terá ${dolar_americano:.2f}.')
print (f'Em peso argentino terá ${peso_argentino:.2f}.')
print (f'Em dólar australiano terá ${dolar_australiano:.2f}.')
print (f'Em dólar canadense terá ${dolar_canadense:.2f}.')
print (f'Em franco suíço terá ${franco_suico:.2f}.')
print (f'Em euro terá ${euro_europeu:.2f}.')
print (f'Em libra esterlina terá ${libra_esterlina:.2f}\n.')
