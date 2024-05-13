#Mostrar os múltiplos de 3 de 0 até 200 
# forma avançada ->
multiplos_de_3 = []
for numero in range(1, 201):
    if numero % 3 == 0:
        multiplos_de_3.append(numero)
formatado = ', '.join(map(str, multiplos_de_3))
print(formatado)
