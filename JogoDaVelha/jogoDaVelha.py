matriz = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
isWinner = False
jogador = 0

for i in range(10):
    # Verificando se tem vencedor
    if isWinner:
        if jogador:
            print('Jogador X venceu!')
        else:
            print('Jogador 0 venceu!')
        break
    # Imprimindo a matriz
    print('    1   2   3')
    for i in range(3):
        print(f'{i+1} {matriz[i]}')
    # Recebendo a a linha  e coluna que o jogador deseja
    linha = int(input('Digite a linha que deseja marcar: ')) - 1
    coluna = int(input('Digite a coluna que deseja marcar: ')) - 1 
    # Verificando se é jogador X ou 0 e se Jogada é invalida
    if jogador and matriz[linha][coluna] ==  '':
        matriz[linha][coluna] = '0'
        jogador = 0
    elif not jogador and matriz[linha][coluna] == '':
        matriz[linha][coluna] = 'X'
        jogador = 1
    else:
        print('Jogada Inválida')
    # Verificando se algum jogador venceu
    for i in range(3):
        if (matriz[i][0] == matriz[i][1] == matriz[i][2]) and '' not in (matriz[i][0], matriz[i][1], matriz[i][2]):
            isWinner = True
        elif (matriz[0][i] == matriz[1][i] == matriz[2][i]) and '' not in (matriz[0][i], matriz[1][i], matriz[2][i]) :
            isWinner = True
        elif (matriz[0][0] == matriz[1][1] == matriz[2][2]) and '' not in (matriz[0][0], matriz[1][1], matriz[2][2]):
            isWinner = True
        elif (matriz[2][0] == matriz[1][1] == matriz[0][2]) and '' not in (matriz[2][0], matriz[1][1], matriz[0][2]):
            isWinner = True
    
if not isWinner:
    print('Velha!')