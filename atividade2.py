class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("depósito de", valor, "realizado com sucesso.")
        else:
            print("valor de depósito inválido.")

    def retirar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print("retirada de", valor, "realizada com sucesso.")
        else:
            print("saldo insuficiente.")

    def exibir_saldo(self):
        print("saldo atual:", self._saldo)


minha_conta = ContaBancaria()
minha_conta.depositar(100)
minha_conta.exibir_saldo()
minha_conta.retirar(50)
minha_conta.exibir_saldo()
