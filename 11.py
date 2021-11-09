"""
Data com mês por extenso. Construa uma função que receba
uma data no formato DD/MM/AAAA e devolva uma string no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide
a data e retorne NULL caso a data seja inválida.
"""


def mesExtenso(dia, mes, ano):
    if mes == 1:
        return f'{dia} de janeiro de {ano}.'


data = '22/01/1985'

d = data[:2]
m = int(data[3:5])
a = data[-4:]

print(mesExtenso(d, m, a))


