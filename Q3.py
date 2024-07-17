'''Escreva  um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa.
Para cada opção, crie uma função.
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.'''

def convert_celsius (temp_celsius):
    convert_celsius1 = (temp_celsius * 1.8) + 32
    return convert_celsius1

def convert_fahrenheit(temp_fahrenheit):
    convert_fahrenheit1 = (temp_fahrenheit - 32) / 1.8
    return convert_fahrenheit1

def menu_escolha():
    print("---- Bem vindos ao menu de conversão de temperatura ----")
    escolher_operação = int (input(f"Digite 1 para converter a temperatura de Celsius em Fahrenheit \nDigite 2 para converter de Fahrenheit em Celsius: "))
    if escolher_operação == 1:
        temp_celsius = float(input("Digite a temperatura desejada em Celsius: "))
        temperatura_convertida1 = convert_celsius(temp_celsius)
        print(f"A temperatura em Celsius é {temp_celsius}°C\nConvertida para Fahrenheit é {temperatura_convertida1:.2f}°F ")
    elif escolher_operação == 2:
        temp_fahrenheit = float(input("Digite a temperatura desejada em Fahrenheit: "))
        temperatura_convertida2 = convert_fahrenheit(temp_fahrenheit)
        print(f"A temperatura em Fahrenheit é {temp_fahrenheit}°F\nConvertida para Celsius é {temperatura_convertida2:.2f}°C")
    else:
        print('Opção inválida.Tente novamente')

menu_escolha()