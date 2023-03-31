# Implemente um programa em python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota valida(maior que 7)
# se não for, ler este valor até que a mesma seja válida

nota = float(input("Digite sua nota: "))

while nota <= 7:
    nota =  float(input("Nota inválida, a nota precisa ser maior que 7 para ser aceita. Insira sua nota: "))
    
print(f'A nota do aluno é {nota:.2f}')
    