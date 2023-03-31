
opcao = None

while opcao != 0:
    print('-------------- MENU CALCULADORA --------------')


    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')
    
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 0:
        print('encerrando calculadora ...')
    elif opcao in (1, 2 ,3, 4): 
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: ')) 
        if opcao == 1:
            print(f'{num1} + {num2} = {(num1 + num2):.2f}')
        elif opcao == 2:
            print(f'{num1} - {num1} = {(num1 - num2):.2f}')
        elif opcao == 3:
            print(f'{num1} x {num2} = {(num1 * num2):.2f}')
        elif opcao == 4:
            print(f'{num1} / {num2}{(num1 / num2):.2f}')
    else:
         print('essa opção não existe, Insira uma das opções disponíveis ')
        