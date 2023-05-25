# Escreva um programa que crie uma lista de palavras e imprima a palavra mais longa e a palavra mais curta da lista

lista = ['jogo', 'banana', 'paralelepipedo', 'água', 'pedra', 'ola']
palavraLonga = lista[0]
palavraCurta = lista[0]

for palavra in lista:
    if len(palavra) > len(palavraLonga):
        palavraLonga = palavra
    elif len(palavra) < len(palavraCurta):
        palavraCurta = palavra

print(f'Palavra Longa {palavraLonga}')
print(f'Palavra Curta {palavraCurta}')

