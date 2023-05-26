# Crie uma matriz de tamanho 3x3 e preencha-a com valores de 1 a 9, Imprima a matriz das tres formas: print(matriz), utilizando um for, utilizando dois for

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

for linha in matriz:
    print(linha)

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
 
# Pratica 2: Utilizando a mesma matriz da pratica anterior, altere os valores nas seguintes posições: [0][0] para 20, [1][2] para 15,
# [2][1] para 19

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

# Pratica 3: Faça as seguintes operações aritméticas com os valores de cada posição e armazene-as em variaveis: soma de [0][0] e [1][0], subtração de [2][2] e [2][1], multiplicação de [0][1] e [2][0], divisão de [1][2] e [0][2], imprima todas as variaveis

soma = matriz[0][0] + matriz[1][0]
subtracao = matriz[2][2] - matriz[2][1]
multiplicacao = matriz[0][1] * matriz[2][0]
divisao = matriz[1][2] / matriz[0][2]
