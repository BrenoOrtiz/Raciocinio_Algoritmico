"""
Faça um programa que possua um vetor que armazene 6 números
inteiros. O programa deve executar os seguintes passos:
a. Armazene os seguintes valores ao vetor: 1, 0, 5, -2, -5, 7.
b. Armazene em uma variável a soma dos valores nas posições 0, 1
e 5. Imprima na tela a soma.
c. Modifique o valor da posição 4 para 100.
d. Imprima na tela cada valor do vetor, um em cada linha.

"""

valores = [1, 0, 5, -2, -5, 7]

soma = valores[0] + valores[1] + valores[5]
print('-' * 30)
print('SOMA:')
print(soma)
print('-' * 30)

valores[4] = 100

print(valores[0])
print(valores[1])
print(valores[2])
print(valores[3])
print(valores[4])
print(valores[5])