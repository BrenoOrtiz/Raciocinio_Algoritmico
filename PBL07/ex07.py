# Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida, imprima apenas os números pares da lista

lista = list(range(1, 101))

for valor in lista:
    if valor % 2 == 0:
        print(valor)