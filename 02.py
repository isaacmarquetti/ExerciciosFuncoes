"""
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba
    um valor n inteiro imprima até a n-ésima linha.
"""


def numeros(n: int):
    for i in range(1, n + 1):
        for v in range(1, i + 1):
            print(v, end='   ')
        print('')


valor = int(input("Digite um valor: "))
numeros(valor)