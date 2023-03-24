# Faça um programa que peça a idade de uma pessoa e informe se ela pode votar ou não.

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar.")