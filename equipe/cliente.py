class Cliente:
    nome_sistema = "Sistema de Barbearia"

    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = valor

    @property
    def maior_de_idade(self):
        return self.idade >= 18

    def apresentar(self):
        return f"Cliente: {self.nome}, telefone: {self.telefone}"

    def fazer_aniversario(self):
        self.idade += 1


if __name__ == "__main__":
    print("Exercício 01:")
    cliente1 = Cliente("João", 25, "99999-1111")
    cliente2 = Cliente("Carlos", 30, "99999-2222")

    print(cliente1.nome)
    print(cliente2.nome)

    cliente1.nome = "João Silva"

    print(cliente1.nome)
    print(cliente2.nome)

    print("\nExercício 02:")
    print(f"Idade antes: {cliente1.idade}")
    cliente1.fazer_aniversario()
    print(f"Idade depois: {cliente1.idade}")

    print("\nExercício 03:")
    try:
        cliente1.idade = -5
    except ValueError as erro:
        print(erro)

    print("\nExercício 04:")
    print(cliente1.nome_sistema)
    print(cliente2.nome_sistema)
    print(Cliente.nome_sistema)

    print("\nExercício 06:")
    print(cliente1.maior_de_idade)