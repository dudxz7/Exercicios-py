# Escreva um programa em Python que gere uma lista com 6 números inteiros aleatórios, entre 1 e 60, e exiba estes números para o usuário.
import random

#Gerar lista com 6 números inteiros aleatórios entre 1 e 60
lista = [random.randint(1, 60) for i in range(6)]
print("Lista original:", lista)

#Ordenar a lista
lista.sort()
print("Lista ordenada:", lista)

#Exibir o maior e o menor valor
print("Maior valor:", max(lista))
print("Menor valor:", min(lista))

#Remover números duplicados
lista = sorted(set(lista))
print("Lista sem valores duplicados:", lista)

#Completar a lista para ter 6 números
while len(lista) < 6:
    lista.append(random.randint(1, 60))
    
print("Lista final:", lista)

