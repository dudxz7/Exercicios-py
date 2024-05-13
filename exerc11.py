# Crie um dicionário que armazene o nome e o telefone de 5 contatos. Escreva um programa que permita ao usuário buscar o telefone de um contato pelo nome.

contatos = {
    'maathzao': '1234-5678',
    'xummp': '9876-5432',
    'marlindo': '1111-2222',
    'yukirito': '3333-4444',
    'dudxz': '1111-1111'
}
nome = input("Digite o nome do contato para buscar o telefone: ")
telefone = contatos.get(nome)
if telefone:
    print(f"O telefone de {nome} é: {telefone}")
else:
    print(f"O contato de {nome} não foi encontrado.")
