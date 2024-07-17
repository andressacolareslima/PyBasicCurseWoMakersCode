'''Crie um dicionário representando contatos(nome,telefone).
Permita ao usuário procurar por um contato pelo nome.'''

lista_contatos = {
    'jujuba' : '1234-4567',
    'salem' : '4002-8922',
    'paçoca': '9876-5432',
    'tom' : '6276-0000',
    'minhoca' :'9999-9999'
}

def procurar (nome, lista_contatos):
    if nome in lista_contatos:
        return f'O nome está na lista. Seu nome é {nome} e telefone {lista_contatos[nome]}'
    else:
        return f'O contato {nome} não foi encontrato. Tente novamente. '
    
nome_contato = input("Digite o contato que deseja procurar: ")
contato_procurado = procurar(nome_contato, lista_contatos)

print(contato_procurado)