# Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela

numeros = [12, 5, 8, 2, 9, 1, 10, 2, 45, 12]
contador  = 0
numerosRepetidos = []

while contador < 10:
    if numeros[contador] in numeros[contador+1::] and numeros[contador] not in numerosRepetidos:
        numerosRepetidos.append(numeros[contador])
        contador += 1
    else:
        contador += 1


print(f'Os numeros repetidos são {numerosRepetidos}')