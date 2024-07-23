horas = int (input ("Quantas horas por semana você pratica atividade física? "))

caloria_media_hora = 5 * 60
horas_mes = horas * 4
caloria_mes = caloria_media_hora * horas_mes

print (f"Se você pratica {horas} horas de exercicios semanais, seu gasto calorico mensal é de aproximadamente {caloria_mes}.")
