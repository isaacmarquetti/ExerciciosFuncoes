"""
Desenha moldura. Construa uma função que desenhe um retângulo usando
os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros,
linhas e colunas, sendo que o valor por omissão é o valor mínimo igual
a 1 e o valor máximo é 20. Se valores fora da faixa forem informados,
eles devem ser modificados para valores dentro da faixa de forma
elegante.
"""


def forma_elegante(lin=1, col=1):
    c = '|'
    l = '-'
    b = '+'
    if lin > 20 or lin <= 0 or col > 20 or col <= 0:
        print("Valor inválido. Forma padrão 5x5")
        print(f"{b}{l * 5}{b}")
        for _ in range(0, 5):
            print(f"{c}{c: >{5 + 1}}")
        print(f"{b}{l * 5}{b}")
    else:
        print(f"{b}{l * col}{b}")
        for _ in range(0, lin):
            print(f"{c}{c: >{col + 1}}")
        print(f"{b}{l * col}{b}")

print("BORDAS (20x20):")
while True:
    try:
        linhas = int(input("Digite o número de linhas: "))
        colunas = int(input("Digite o número de colunas: "))
        forma_elegante(linhas, colunas)
        break
    except ValueError:
        print("Erro! Digite um valor de 0 a 20.")