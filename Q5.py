'''Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.'''

def contador_vogais (frases):
    vogais = 'aeiouAEIOU'

    contador = 0

    for i in frases:
        if i in vogais:
            contador +=1
    return contador

frases1 = input("Digite a frase e/ou palavra desejada: ")
contador_vogais1 = contador_vogais(frases1)
print(f'A frase e/ou palavra "{frases1}", possui {contador_vogais1} vogais. ')