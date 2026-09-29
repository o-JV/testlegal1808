import pytest

from cliente import Cliente


def test_idade_negativa_na_criacao_levanta_erro():
    with pytest.raises(ValueError):
        Cliente("João", -5, "99999-1111")


def test_idade_negativa_no_setter_levanta_erro():
    cliente = Cliente("João", 25, "99999-1111")
    with pytest.raises(ValueError):
        cliente.idade = -1


def test_mensagem_do_erro():
    cliente = Cliente("João", 25, "99999-1111")
    with pytest.raises(ValueError, match="não pode ser negativa"):
        cliente.idade = -10


def test_idade_valida_funciona():
    cliente = Cliente("João", 25, "99999-1111")
    assert cliente.idade == 25