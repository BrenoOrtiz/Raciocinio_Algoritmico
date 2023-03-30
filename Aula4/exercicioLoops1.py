# imprima na tela a tabuada de um numero inteiro lido pelo teclado

numero = int(input("Insira um numero: "))
i = 1

while i <= 10:
    print(f'{numero}*{i} = {numero * i}')
    i += 1
    
    