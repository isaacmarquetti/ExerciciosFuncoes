"""
Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos.
"""


def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    print(f'A soma dos 3 valores é {soma}.')


num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
somar(num1, num2, num3)