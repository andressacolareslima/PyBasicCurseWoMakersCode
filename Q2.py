"""Faça um Programa que peça as quatro notas de 5 alunos,
calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.""" 

tamanho_lista = 4
alunos_aprovados = 0
numero_alunos = 5

for i in range(numero_alunos):
    notas = input(f"Digite as {tamanho_lista} notas, separadas por vírgula, do {i+1} aluno: ")
    numeros_convertidos = [float(num) for num in notas.split(',')]

    media = sum(numeros_convertidos) / tamanho_lista

    if media >=7.0:
        alunos_aprovados+=1

print(f'A quantidade de alunos aprovados é {alunos_aprovados}.')
            

    