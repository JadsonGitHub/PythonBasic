class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return (
            "Cliente:\n"
            + "    "
            + str(self.cliente).replace("\n", "\n    ")
            # + '\n'.join(f'    {line}' for line in str(self.cliente).splitlines())
            + "\nSaldo: "
            + str(self.saldo)
            + "\nLimite: "
            + str(self.limite)
        )

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito de R$", valor)
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor - self.saldo <= self.limite:
            self.saldo -= valor
            print("Saque de R$", valor)
        else:
            print("Valor acima do limite")

    def extrato(self):
        return self.saldo
