""" Faça um programa que preenche um vetor de 50 posições com valores
aleatórios entre 0 e 20 e encontre:
Obs: Para fazer um vetor de tamanho 50 preenchido com 0 é possível fazer:
vetor = [0] * 50. Note que o valor 50 também pode ser substituído por uma variável
qualquer.
a. A soma dos valores armazenados no vetor.
b. O número de ocorrências do valor 9.
c. O maior valor armazenado no vetor.
d. O menor valor armazenado no vetor
"""

import random

vetor = [0] * 50

for i in range(50):
    vetor[i] = random.randint(0, 20)

print("Vetor: ", vetor)

maior_valor = max(vetor)
print("Maior valor: ", maior_valor)

menor_valor = min(vetor)
print("Menor valor: ", menor_valor)

media_valores = sum(vetor) / len(vetor)
print("MÃ©dia dos valores: ", media_valores)

qtd_pares = 0
for valor in vetor:
    if valor % 2 == 0:
        qtd_pares += 1
print("Quantidade de valores pares: ", qtd_pares)