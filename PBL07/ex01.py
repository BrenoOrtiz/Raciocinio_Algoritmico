# Escreva um programa que crie uma lista com números aleatórios e a imprima na tela

from random import randint

lista = [randint(1, 50) for i in range(randint(1, 15))]

print(lista)