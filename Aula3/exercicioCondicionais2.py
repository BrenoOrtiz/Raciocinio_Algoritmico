# Leia a média de um estudante e imprima se ele foi aprovado
quantidadeProva = float(input('Quantas avaliações foram feitas?'))

notas = [float(input('Digite sua nota: ')) for num in range(quantidadeProva)]

media = sum(notas)/len(notas)

if media >= 7:
    print('Você passou')
    print(f'Sua média é: {media:.2f}')
else:
    print('Você reprovou')
    print(f'Sua média é {media:.2f}')