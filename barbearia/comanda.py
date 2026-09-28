"""Domínio da barbearia: a Comanda é a entidade central.

Antes (Aula 4), a comanda era uma lista solta passada para cada função:
    itens_validos(comanda)
    subtotal(comanda)

Agora, a lista de itens vive em self e as duas funções viram métodos:
    comanda.itens_validos()
    comanda.subtotal()
"""

from decimal import Decimal

CATALOGO = {"corte": 25.00, "barba": 18.00, "sobrancelha": 10.00}


class Comanda:
    """Comanda de atendimento com os serviços pedidos pelo cliente."""

    def __init__(self, itens=None):
        self.itens = list(itens) if itens else []

    def adicionar_item(self, item):
        if item not in CATALOGO:
            raise ValueError(
                f"Serviço inválido: {item!r}. Opções: {', '.join(CATALOGO)}."
            )
        self.itens.append(item)

    def itens_validos(self):
        validos = []
        for item in self.itens:
            if item in CATALOGO:
                validos.append(item)
        return validos

    def subtotal(self):
        soma = Decimal("0.00")
        for item in self.itens_validos():
            soma += Decimal(str(CATALOGO[item]))
        return soma

    def __repr__(self):
        return f"Comanda({self.itens!r})"


def desconto(comanda, valor):
    if valor >= Decimal("30.00"):
        return valor * Decimal("0.10")
    return Decimal("0.00")


def fechar(comanda):
    sub = comanda.subtotal()
    desc = desconto(comanda, sub)
    tot = sub - desc
    return {"subtotal": sub, "desconto": desc, "total": tot}
