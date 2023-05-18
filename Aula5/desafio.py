from random import randint

numeros  = []
numerosSorteio = []
numerosAcertados = []

for i in range(6):
    numeros.append(int(input("Escolha um numero de 1 a 60: ")))
    numeroRandom = randint(1, 60)
    numerosSorteio.append(numeroRandom)
    if numeros[i] == numerosSorteio[i]:
        numerosAcertados.append(numeroRandom)
    

print(f'Você acertou {numerosAcertados}')
print(f'Os numeros sorteados foram {numerosSorteio}')
