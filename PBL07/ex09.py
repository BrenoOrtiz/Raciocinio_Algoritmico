# Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de uma determinada letra e informe se ele acertou ou errou

from random import shuffle, choice

alfabeto = ['a', 'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k', 'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u', 'v','w', 'x', 'y', 'z']
shuffle(alfabeto)
letra = choice(alfabeto)

print(f'Advinhe a posição da letra {letra}')
posicao = int(input('Digite a posição: '))

if posicao == alfabeto.index(letra):
    print('Você acertou!')
else:
    print('Você errou!')

