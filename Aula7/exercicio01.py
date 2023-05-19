"""
Crie um algoritmo que possua duas listas vazias chamadas
numerosJogador1 e numerosJogador2. Em seguida, randomize um
número entre 1 e 6 (vamos simular um dado) e armazene o valor na lista.
Repita esse processo 3 vezes (como se 3 dados tivessem sido jogados)
para cada um dos jogadores. Por último, some os valores de cada
jogador, e exiba na tela qual jogador foi o vencedor. Vence aquele que
tiver a soma com maior número.

"""

from random import randint

numerosJogador1 = []
numerosJogador2 = []

for i in range(3):
    numerosJogador1.append(randint(1, 6))
    numerosJogador2.append(randint(1, 6))
    
sumNumerosJogador1 = sum(numerosJogador1)
sumNumerosJogador2 = sum(numerosJogador2)    
    
if sumNumerosJogador1 > sumNumerosJogador2:
    print(f' Jogador 1 ganhou com {sumNumerosJogador1} pontos')
elif sumNumerosJogador1 == sumNumerosJogador2:
    print(f'Empate')
else:
    print(f'Jogador 2 ganhou com {sumNumerosJogador2} pontos')
