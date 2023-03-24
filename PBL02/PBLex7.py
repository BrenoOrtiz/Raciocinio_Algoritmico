# Faça um programa que peça as notas de três provas de um aluno e calcule a média. Informe se o aluno está aprovado (média maior ou igual a 7), em recuperação (média entre 5 e 7) ou reprovado (média abaixo de 5).

# input
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
n4 = float(input('digite a quarta nota: '))

# process
media = (n1 + n2 + n3 + n4) / 4

# output
if media >= 7:
    print('voce passou com media: ', media)

elif media >= 4 and media < 7:
    print('voce esta de recuperaÃ§ao com media: ', media)

else:
    print('voce nao passou com media: ', media)