from random import randint

print('1 - Humano X Humano')
print('2 - Humano X Computador')
print('3 - Computador X Computador')
print()


condicao = True
opcoes = ['pedra', 'papel', 'tesoura']
modalidade = int(input('Escolha sua modalidade: '))


while condicao:
    if modalidade == 1:
        print((' -'*20), '\n Jogador 1 \n', ('- '*20),  f' \n Escolha entre \n Pedra - Digite 0 \n Papel - Digite 1 \n Tesoura - Digite 2')
        input1 = int(input('->'))
        print((' -'*20), '\n Jogador 2 \n', ('- '*20),  f' \n Escolha entre \n Pedra - Digite 0 \n Papel - Digite 1 \n Tesoura - Digite 2')
        input2 = int(input('->'))
    elif modalidade == 2:
        print((' -'*20), '\n Jogador 1 \n', ('- '*20),  f' \n Escolha entre \n Pedra - Digite 0 \n Papel - Digite 1 \n Tesoura - Digite 2')
        input1 = int(input('->'))
        print((' -'*20), '\n Computador \n', ('- '*20),  f'\n  Escolha do Computador')
        input2 = randint(0, 2)
    elif modalidade == 3:
        print((' -'*20), '\n Computador \n', ('- '*20),  f'\n  Escolha do Computador')
        input1 = randint(0, 2)
        print((' -'*20), '\n Computador \n', ('- '*20),  f'\n  Escolha do Computador')
        input2 = randint(0, 2) 
    if input1 == input2:
        print('Empate!')
        print(f'Jogador 1 escolheu {opcoes[input1]} e Jogador 2 escolheu {opcoes[input2]}')
    elif input1 in (0, 2) and input2 in (0, 2):
        print()
        if input1 == 0:
            print('Jogador 1 Ganhou!!!')
        else:
            print('Jogador 2 Ganhou!!!')
        print(f'Jogador 1 escolheu {opcoes[input1]} e Jogador 2 escolheu {opcoes[input2]}')
        condicao = bool(int(input('Deseja Continuar Jogando? \n Sair - 0 \n Continuar - 1 \n')))
    elif input1 > input2:
        print()
        print('Jogador 1 Ganhou!!!')
        print(f'Jogador 1 escolheu {opcoes[input1]} e Jogador 2 escolheu {opcoes[input2]}')
        condicao = bool(int(input('Deseja Continuar Jogando? \n Sair - 0 \n Continuar - 1 \n')))
    else:
        print()
        print('Jogador 2 Ganhou!!!')
        print(f'Jogador 1 escolheu {opcoes[input1]} e Jogador 2 escolheu {opcoes[input2]}')
        condicao = bool(int(input('Deseja Continuar Jogando? \n Sair - 0 \n Continuar - 1 \n')))
    
    
        