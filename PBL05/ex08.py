# Faça um algoritmo que leia um número positivo e imprima seus divisores

numero = int(input('Digite um número: '))

if numero <= 0:
    print('O número deve ser positivo.')
else:
    print('Os divisores do', numero,'são:')

for i in range(1, numero):
    if numero % i == 0:
        print(i)