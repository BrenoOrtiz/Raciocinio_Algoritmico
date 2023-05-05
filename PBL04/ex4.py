# Crie um programa que lê 6 valores inteiros, armazene-os em um vetor e, em seguida, mostre na tela os valores lidos na ordem inversa

numeros = [0,0,0,0,0,0]

n0 = int(input("Digite um numero: "))
numeros[0] = n0
n1 = int(input("Digite um numero: "))
numeros[1] = n1
n2 = int(input("Digite um numero: "))
numeros[2] = n2
n3 = int(input("Digite um numero: "))
numeros[3] = n3
n4 = int(input("Digite um numero: "))
numeros[4] = n4
n5 = int(input("Digite um numero: "))
numeros[5] = n5

numeros.reverse()
print(numeros)