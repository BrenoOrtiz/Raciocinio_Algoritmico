# Crie um vetor [5, 7, 12, 2, 9, 21] e imprima ele e cada um dos seus valores

numeros = [5, 7, 12 ,2, 9, 21]

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])

# Na mesma atividade da pratica 1 altere os valores 7 e 2 para 17 e 22 e imprima o vetor, altere também os valores dos indices 2 e 4 para 1 e 29 e imprima o vetor

numeros = [5, 7, 12 ,2, 9, 21]

numeros[1], numeros[3] = 17, 22
print(numeros)

numeros[2], numeros[4] = 1, 29
print(numeros)

# some os valores 21 e 29, subtraia os valores 22 e 17, multiplique os valores dos indices 0 e 5 e divida os valores dos indices 3 e 2

soma  = numeros[5] + numeros[4]
subtracao = numeros[3] - numeros[1]
multiplicacao = numeros[0] * numeros[5]
divisao = numeros[3] / numeros[2]

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)

# percorra o vetor utilizando while e imprima cada valor multiplicado por 2

indice = 0
while indice < 6:
    print(numeros[indice]*2)
    indice += 1
    

