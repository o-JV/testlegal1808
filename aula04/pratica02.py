CATALOGO = {
    "Corte": 20.00,
    "Barba": 15.00,
    "Sobrancelha": 10.00
}


def itens_validos(comanda):
    validos = []
    for item in comanda:
        if item in CATALOGO:
            validos.append(item)
        return validos

def subtotal(comanda):
    for item in itens_validos()