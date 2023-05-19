from random import choice

palavras = ['python', 'jogar', 'estudar', 'vetor', 'bola', 'tempo']
palavraSecreta = choice(palavras)
tentativas = 10
letrasAcertadas = ['_'] * len(palavraSecreta)

for i in range(tentativas):
    letra = input('Digite uma letra: ').lower()
    tentativasRestantes = tentativas - (i+1)
    if letra in palavraSecreta:
        indiceLetra = palavraSecreta.index(letra)
        print(f'Tentativas restantes: {tentativasRestantes}')
        letrasAcertadas[indiceLetra] = letra
        print(f'Palavra: {str(letrasAcertadas)[1:-1]}')
    else:
        print(f'Tentativas restantes: {tentativasRestantes}')
        print(f'Palavra: {str(letrasAcertadas)[1:-1]}')
        print(f'A letra digitada não existe')
    if '_' not in letrasAcertadas:
        print('Parabéns! Você acertou a palavra secreta')
        break
    elif '_' in letrasAcertadas and tentativasRestantes == 0:
        print('Suas tentativas Acabaram')
        