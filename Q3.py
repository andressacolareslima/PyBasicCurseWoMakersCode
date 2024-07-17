'''Crie um dicionário representando um carrinho de compras.
Adicione produtos(chaves)e quantidades(valores)ao carrinho.Calcule o total do carrinho de compra.'''

carrinho_compras = {
    'carne de frango': {'quantidade': 3, 'valor':20.32},
    'arroz': {'quantidade': 5, 'valor':5.25},
    'feijão': {'quantidade': 3, 'valor':8.98},
    'refrigerante': {'quantidade': 1, 'valor':10.11},
    'detergente': {'quantidade': 2, 'valor': 2.89}
}

def calcular_carrinho (carrinho_compras):
    total = 0
    for i, x in carrinho_compras.items():
        quatidade = x ['quantidade']
        preco = x ['valor']
        total += quatidade*preco
    return total

qnt_compras = calcular_carrinho(carrinho_compras)

print(f"O total de compras desse carinho é em reais R$ {qnt_compras:.2f}")