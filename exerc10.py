#Escreva um programa que solicite ao usuário que insira o nome de cinco países e suas respectivas capitais. Armazene essas informações em um dicionário e, em seguida, imprima o dicionário.

paises = {}
for x in range(5):
    pais = input("Digite o nome do país: ")
    capital = input("Digite a capital de " + pais + ": ")
    paises[pais] = capital

#Imprimindo o dicionário
print("\nDicionário de países e capitais:")
for pais, capital in paises.items():
    print(f"{pais}: {capital}")
