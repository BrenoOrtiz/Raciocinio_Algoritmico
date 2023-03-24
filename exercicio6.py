# Escreva um código que calcule o preço de um produto por quilo

valor = float(input('Digite o valor do produto: '))
peso = float(input('Digite o peso do produto: '))

preco = valor * peso

print(f'O preço final do produto é R$ {preco:.2f}')

