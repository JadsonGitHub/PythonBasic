"""
EXERCICIO:
Faça um formulario que pergunte, nome, cpf, endereço, idade, altura e telefone e imprima em um relatorio
"""

print("\nPROGRAMA FORMULARIO\n")

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
rua = input("Digite seu Endereço: ")
age = input("Digite sua idade: ")
size = input("Digite sua altura: ")
tel = input("Digite seu telefone: ")

print("\nRELATÓRIO DO CLIENTE\n")
print("Nome do cliente:\t", nome)
print("CPF do cliente: \t", cpf)
print("Endereço do cliente:\t", rua)
print("Idade do cliente:\t", age, "anos")
print("Altura do cliente:\t", size, "m")
print("Telefone do cliente:\t", tel, "\n")
