from decimal import Decimal

import pytest

from barbearia import Comanda, desconto, fechar


def test_itens_validos_filtra_itens_fora_do_catalogo():
    comanda = Comanda(["corte", "barba", "item_invalido"])
    assert comanda.itens_validos() == ["corte", "barba"]


def test_itens_validos_comanda_vazia():
    assert Comanda().itens_validos() == []


def test_subtotal_soma_precos_dos_itens_validos():
    comanda = Comanda(["corte", "barba", "item_invalido"])
    assert comanda.subtotal() == Decimal("43.00")


def test_subtotal_comanda_vazia_e_zero():
    assert Comanda().subtotal() == Decimal("0.00")


def test_desconto_aplica_10_por_cento_a_partir_de_30():
    assert desconto(Comanda(), Decimal("43.00")) == Decimal("4.300")


def test_desconto_zero_abaixo_de_30():
    assert desconto(Comanda(), Decimal("25.00")) == Decimal("0.00")


def test_fechar_com_desconto():
    resultado = fechar(Comanda(["corte", "barba", "item_invalido"]))
    assert resultado["subtotal"] == Decimal("43.00")
    assert resultado["desconto"] == Decimal("4.300")
    assert resultado["total"] == Decimal("38.700")


def test_fechar_sem_desconto():
    resultado = fechar(Comanda(["corte"]))
    assert resultado["total"] == Decimal("25.00")


def test_adicionar_item_valido():
    comanda = Comanda()
    comanda.adicionar_item("sobrancelha")
    assert comanda.itens == ["sobrancelha"]


def test_adicionar_item_invalido_levanta_value_error():
    comanda = Comanda()
    with pytest.raises(ValueError, match="Serviço inválido"):
        comanda.adicionar_item("massagem")


def test_item_invalido_nao_entra_na_comanda():
    comanda = Comanda(["corte"])
    with pytest.raises(ValueError):
        comanda.adicionar_item("massagem")
    assert comanda.itens == ["corte"]


def test_comandas_tem_estados_independentes():
    a, b = Comanda(["corte"]), Comanda()
    b.adicionar_item("barba")
    assert a.itens == ["corte"]