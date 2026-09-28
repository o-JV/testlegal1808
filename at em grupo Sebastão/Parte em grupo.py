class Cliente:
    # Atributo de classe
    nome_sistema = "Sistema de Barbearia"

    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade  # Passa pelo @idade.setter para validar a idade na criação
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
        return f"Cliente: {self.nome}, Idade: {self.idade}, Telefone: {self.telefone}"


# 01 - Dois objetos, dois estados
cliente1 = Cliente("João", 25, "99999-1111")
cliente2 = Cliente("Carlos", 30, "99999-2222")

print("Exercício 01:")
print(cliente1.nome)
print(cliente2.nome)

cliente1.nome = "João Silva"

print(cliente1.nome)
print(cliente2.nome)


# 02 - Método
print("\nExercício 02:")
print(cliente1.apresentar())


# 03 - Valor inválido
print("\nExercício 03:")
try:
    cliente1.idade = -5
except ValueError as erro:
    print(erro)


# 04 - Atributo de classe
print("\nExercício 04:")
print(cliente1.nome_sistema)
print(cliente2.nome_sistema)


# 06 - Property
print("\nExercício 06:")
print(cliente1.maior_de_idade)