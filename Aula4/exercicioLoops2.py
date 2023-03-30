# Implemente um programa em python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota valida(maior que 7)
# se não for, ler este valor até que a mesma seja válida

nota = float(input("Digite sua nota: "))
i = 0

while i < 10:
    if nota < 7:
        print(f'nota inválida {nota}')
        nota += 1
        i += 1
    else:
        print(f'nota valida {nota}')
        i += 11
    