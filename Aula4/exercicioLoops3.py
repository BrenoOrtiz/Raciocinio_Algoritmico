#   Implemente um programa em python para ler do teclado números. Caso o usuário forneça um numero igual a -1, o programa deve fornecer a média dos numeros e encerrar;

i = 0
sum = 0

while i != -1:
    number = int((input("Digite um numero: ")))
    if number == -1:
        print(f'A média é: {(sum/i):.2f}')
        i = -1
    else:
        sum += number
        i += 1
    
