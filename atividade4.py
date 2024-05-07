class Funcionario:
    def _init_(self, nome, id, salario):
        self._nome = nome
        self._id = id
        self._salario = salario

    def alterar_salario(self, novo_salario):
        self._salario = novo_salario

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def get_salario(self):
        return self._salario


class Departamento:
    def _init_(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print("Nome:", funcionario.get_nome())
            print("ID:", funcionario.get_id())
            print("Salário:", funcionario.get_salario())
            print("-" * 20)


if __name__ == "_main_":
    funcionario1 = Funcionario("João", 1, 3000)
    funcionario2 = Funcionario("Maria", 2, 3500)
    funcionario3 = Funcionario("Pedro", 3, 3200)

    departamento = Departamento()

    departamento.adicionar_funcionario(funcionario1)
    departamento.adicionar_funcionario(funcionario2)
    departamento.adicionar_funcionario(funcionario3)

    departamento.listar_funcionarios()
