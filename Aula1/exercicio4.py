# Escreva um código que calcule a média entre n notas
 
quantidadeNotas = int(input("Insira a quantidade de avaliações:"))
notas = []

for i in range(quantidadeNotas):
    notas.append(float(input("Insira sua nota: ")))

media = sum(notas)/quantidadeNotas 
print(f'Sua média é: {media:.2f}')