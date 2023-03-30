# Implemente um programa em python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado

n = int(input('Digite um numero: '))
count = 1
sum = 0

while count <= n:
    sum += count
    count += 1

print(f'O somatório é {sum}')