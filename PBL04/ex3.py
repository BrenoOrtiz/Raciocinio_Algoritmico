"""
Faça um programa que preenche um vetor com valores inteiros até que
o usuário digite um valor negativo (o valor negativo não deve ser
inserido no vetor). Imprima:
a. O vetor.
b. A quantidade de valores maiores que 5.
c. A soma dos valores pares armazenados no vetor.
d. A soma dos valores ímpares armazenados no vetor.
e. A quantidade total de valores armazenados no vetor.

"""

valores = []
valor = int(input("Digite um valor inteiro (digite um valor negativo para parar): "))
while valor >= 0:
    valores.append(valor)
    valor = int(input("Digite um valor inteiro (digite um valor negativo para parar): "))

print("Lista: ", valores)

i = 0
maiores_que_cinco = 0
while i < len(valores):
    if valores[i] > 5:
        maiores_que_cinco += 1
    i += 1
print("Quantidade de valores maiores que 5: ", maiores_que_cinco)


i = 0
soma_pares = 0
soma_impares = 0
while i < len(valores):
    if valores[i] % 2 == 0:
        soma_pares += valores[i]
    else:
        soma_impares += valores[i]
    i += 1
print("Soma dos valores pares: ", soma_pares)
print("Soma dos valores Ã­mpares: ", soma_impares)

quantidade_total = len(valores)

print("Quantidade total de valores: ", quantidade_total)