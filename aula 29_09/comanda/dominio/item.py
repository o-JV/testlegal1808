class Item:
    def __init__(self, nome, preco):
        if not nome or not nome.strip():
            raise ValueError("O nome não pode ser vazio")
        if preco < 0:
            raise ValueError("O preço não pode ser negativo")
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"{self.nome}: R$ {self.preco}"


class Bebida(Item):
    def __init__(self, nome, preco, volume_ml):
        super().__init__(nome, preco)
        self.volume_ml = volume_ml

    def descricao(self):
        return f"{super().descricao()} ({self.volume_ml} ml)"


class Prato(Item):
    def __init__(self, nome, preco, tempo_preparo):
        super().__init__(nome, preco)
        self.tempo_preparo = tempo_preparo