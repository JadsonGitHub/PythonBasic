"""
EXERCICIO:
Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa. O programa irá
perguntar o nome das pessoas e fazer uma lista
de convidados e imprimir
"""

print("\nPROGRAMA LISTA CONVIDADOS\n")

quantidade = int(input("Digite a quantidade de convidados: "))

print()

convidados = []

i = 0

while i < quantidade:
    convidados.append(input(f"Digite o nome do {i + 1}° convidado: "))
    i += 1

print()
for convidado in convidados:
    print(convidado)
print()
