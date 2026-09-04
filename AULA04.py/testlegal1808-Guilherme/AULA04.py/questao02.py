from decimal import Decimal

CATALOGO = {"corte": 25.00, "barba": 18.00, "sobrancelha": 10.00}


def itens_validos(comanda):
  validos = []
  for item in comanda:
    if item in CATALOGO:
      validos.append(item)
  return validos


def subtotal(comanda):
  itens = itens_validos(comanda)
  soma = Decimal("0.00")
  for item in itens:
    soma += Decimal(str(CATALOGO[item]))
  return soma


def desconto(comanda, valor):
  if valor >= Decimal("30.00"):
    return valor * Decimal("0.10")
  return Decimal("0.00")


def fechar(comanda):
  sub = subtotal(comanda)
  desc = desconto(comanda, sub)
  tot = sub - desc

  return {"subtotal": sub, "desconto": desc, "total": tot}


minha_comanda = ["corte", "barba", "item_invalido"]
resultado = fechar(minha_comanda)

print(f"Subtotal: R$ {resultado['subtotal']:.2f}")
print(f"Desconto: R$ {resultado['desconto']:.2f}")
print(f"Total:    R$ {resultado['total']:.2f}")