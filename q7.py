ganha_hora = float (input("Quanto você recebe por horas trabalhadas (em R$)? "))
qnts_horas = float (input("Quantas horas você trabalha mensalmente? "))

salario = ganha_hora * qnts_horas 
print (f'Se você trabalha {qnts_horas} horas por mês e recebe {ganha_hora} por hora trabalhada, seu salário mensal é de R${salario}, aproximadamente. ')