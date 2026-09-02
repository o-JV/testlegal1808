CATALOGO = {
    "corte": 25.00,
    "barba": 18.00,
    "sobrancelha": 10.00
}


def itens_validos(comanda):
    validos = []
    for item in comanda:
        if item in catalogo:
            validos.append(item)
        return validos

def subtotal(comanda):
    for item in itens_validos        