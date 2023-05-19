"""
Crie um algoritmo que peça ao usuário para informar 5 valores inteiros
positivos e armazene-os em uma lista com nome qualquer. Em seguida,
crie uma nova lista ordenada dos valores e uma nova lista com os valores
ordenados em ordem inversa. Imprima na tela:
a. As três listas
b. O tamanho da lista
c. O menor valor informado
d. O maior valor informado
e. A soma de todos os valores da lista
Exercício

"""

lista1 = [int(input('Insira um numero inteiro positivo: ')) for i in range(5)]
lista2 = sorted(lista1)
lista3 = reversed(lista2)

print(f'lista 1: {lista1}')
print(f'lista Ordenada: {lista2}')
print(f'lita Ordenada Inversa: {list(lista3)}')
print(f'Tamanho da lista: {len(lista1)}')
print(f'Menor valor {min(lista1)}')
print(f'Maior valor {max(lista1)}')
print(f'Soma dos valores da lista {sum(lista1)}')
    
