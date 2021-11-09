"""
Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
"""


def reverso(n):
    return int(n[::-1])


num = input("Digite um número: ")

print(reverso(num))
