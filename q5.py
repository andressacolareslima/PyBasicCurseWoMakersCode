distancia = float (input("Digite a distância aproximada do destino (em KM): "))

aviao = distancia / 600
carro = distancia / 100
onibus = distancia / 80

print ("Tempo aproximado de cada viagem é: ")
print (f'Avião: {aviao:.2f} horas')
print (f'Carro: {carro:.2f} horas')
print (f'Ônibus: {onibus:.2f} horas')