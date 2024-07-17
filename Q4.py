'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.'''

pontuacao_exame = input("De 0 a 10 digite sua pontuação no exame: ")

if pontuacao_exame >='7':
    print("Você foi aprovado. Parábens. ")
else:
    print("Você foi reprovado. ")