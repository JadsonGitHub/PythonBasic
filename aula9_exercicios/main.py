"""
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo
"""

from conta import Conta
from cliente import Cliente

print("\nSIMULACAO BANCO\n")

c = Cliente("Ali", "000.000.000-00", 20)

print(c, "\n")

cc = Conta(c, 100, 1000)

print(cc, "\n")

print(cc.extrato())

cc.depositar(1000)

print(cc.extrato())

cc.sacar(500)

print(cc.extrato())

cc.sacar(2000)

print(cc.extrato())
