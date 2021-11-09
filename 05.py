"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto
sobre vendas.
"""


def somaImposto(taxa_imposto, valor):
    return valor + (valor / 100 * taxa_imposto)


valor = float(input("Digite o valor do produto: R$"))
porc = float(input("Informe o imposto sobre a venda (%): "))

print(f"O valor final com imposto de {porc:.0f}% é de R${somaImposto(porc, valor):.2f}.")