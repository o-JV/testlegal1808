CATALOGO = {
    "corte": 20.00,
    "barba": 15.00, 
    "sobrancelha": 10.00
}


def itens_validades(comanda):
    validos = []
    for item in comanda:
        if item in CATALOGO:
            validos.append(item)
        return validos

def subtotal(comanda):
    for