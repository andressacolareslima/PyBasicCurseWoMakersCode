peso = float (input("Digite o seu peso (em KG) : "))
altura = float (input ("Agora, digite sua altura (em M): "))

imc = peso / (altura*altura)

print (f"Seu peso é {peso} kg e sua altura é {altura} m. Com isso seu IMC será de aproximadamente {imc:.2f}.")