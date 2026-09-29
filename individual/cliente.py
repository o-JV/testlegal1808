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