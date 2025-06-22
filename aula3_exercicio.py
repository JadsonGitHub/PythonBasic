"""
EXERCICIO:
Faça um programa que pergunte a idade, peso e altura
de uma pessoa e decide se ela esta apta a entrar no
Exercito.
Os indices sao: maior de 18anos, >= 60kg e >= 170cm
"""

print("\nPROGRAMA QUALIFICAÇAO EB\n")

age = int(input("Digite sua Idade (anos):\t"))
peso = float(input("Digite seu Peso (kg):\t\t"))
altura = float(input("Digite sua Altura (cm):\t\t"))

if age < 18:
    print("\nIdade abaixo do permitido")
if peso < 60:
    print("\nPeso abaixo do permitido")
if altura < 170:
    print("\nAltura abaixo do permitido")
if age >= 18 and peso >= 60 and altura >= 170:
    print("\nAPTO\n")
else:
    print("\nINAPTO\n")
