'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

calculo = float(input("Digite o salário bruto em reais: R$"))

if calculo <=1903.98:
    liquido = 0
elif calculo >= 1903.99 and calculo <=2826.65:
    liquido = 7.5
elif calculo > 2826.65 and calculo <=3751.05:
    liquido = 15
elif calculo > 3751.05 and calculo <=4664.68:
    liquido = 22.5
else:
    liquido = 27.5

imposto = calculo * liquido / 100
salario_liquido = calculo - imposto

print(f'O sálario liquido em reais é R${salario_liquido:.2f}')