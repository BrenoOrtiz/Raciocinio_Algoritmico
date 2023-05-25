# Escreva um programa que crie duas listas, uma com os números pares de 1 a 10 e outra com os números ímpares de 1 a 10. Em seguida, junte as duas listas em uma terceira lista e a imprima na tela

pares = [valor for valor in range(1, 11) if valor % 2 == 0]
impares = [valor for valor in range(1, 11) if valor % 2 != 0]

lista = []
lista.extend(impares)
lista.extend(pares)

print(lista)
