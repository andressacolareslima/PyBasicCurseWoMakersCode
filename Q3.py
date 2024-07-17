''' Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

while True:
    notas = int(input('Digite a nota: '))
    if 0<= notas <=10:
        print("Nota valida. ")
        break
    else: 
        print("Digite uma nota válida. ")
