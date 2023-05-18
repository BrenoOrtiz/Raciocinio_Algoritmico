# Utilizando a estrutura de repetição for, faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] quantos deles estão fora do intervalo.

numsIntervalo = 0
numsFora = 0

for i in range(1, 11):
    num = int(input('Digite um numero: '))
    if num in range(10, 21):
        numsIntervalo += 1
    else:
        numsFora += 1
        

print(f'{numsIntervalo} numeros dentro do intervalo 10 a 20')
print(f'{numsFora} numeros fora do intervalo 10 a 20')

