"""
EXERCICIO:
Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior e do menor numero dentro dessa colecao
"""

print("\nMAIOR E MENOR NÚMERO\n")

colecao = []

size = int(input("Digite o tamanho da coleçao: "))

for i in range(size):
    valor = float(input(f"Digite o {i + 1}° valor: "))
    colecao.append(valor)


def maior_menor(colecao):
    extremos = [colecao[0], colecao[0]]

    for item in colecao:
        if item > extremos[0]:
            extremos[0] = item

        if item < extremos[1]:
            extremos[1] = item

    return extremos


print("O maior numero é", maior_menor(colecao)[0])
print("O menor numero é", maior_menor(colecao)[1])
print()
