# Escreva um programa que receba 10 números do teclado e exiba a quantidade de números pares e ímpares lidos.

i = 0
pares = 0
impares = 0

while i < 10:
    num = int(input('Digite um numero: '))
    i += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'{pares} números pares')
print(f'{impares} números ímpares')

