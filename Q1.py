"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?
"Esteve no local do crime? 
Mora perto da vítima?
"Devia para a vítima?
Já trabalhou com a vítima?
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2questões ela deve ser classificada como""Suspeita"",
entre 3 e 4 como""Cúmplice""
e 5 como""Assassino"".Caso contrário,ele será classificado como""Inocente""."""

print ("Para nós ajudar responta s para Sim e n para Não ")

lista = [ 
    "Telefonou para vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for i in lista:
    resposta = input(i + "(s/n)").strip().lower()
    if resposta == 's':
        respostas_positivas +=1

if respostas_positivas == 2:
    print("Suspeito")
elif respostas_positivas ==3 or respostas_positivas ==4:
    print("Cúmplice")
elif respostas_positivas ==5:
    print ("Assassino")
else:
    print ("Inocente")