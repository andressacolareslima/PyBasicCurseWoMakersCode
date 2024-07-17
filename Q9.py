'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''
pares = 0
impares = 0

while True:
    numeros = int(input("Digite um número: "))
    if numeros == 0:
        break
    elif numeros < 0:
        print("Você deve inserir apenas números positivos. Tente novamente. ")
    else:
        if numeros % 2 == 0:
            pares += 1
        else:
            impares +=1
print (f'O número de pares inseridos é: {pares}')
print (f'O número de ímpares inseridos é: {impares}')