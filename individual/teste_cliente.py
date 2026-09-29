import pytest

from cliente import Cliente


@pytest.fixture
def cliente():
    return Cliente("João", 25, "99999-1111")


def test_criacao_guarda_atributos(cliente):
    assert cliente.nome == "João"
    assert cliente.idade == 25
    assert cliente.telefone == "99999-1111"


def test_apresentar(cliente):
    assert cliente.apresentar() == "Cliente: João, telefone: 99999-1111"


def test_maior_de_idade(cliente):
    assert cliente.maior_de_idade is True


def test_menor_de_idade():
    menor = Cliente("Pedro", 15, "99999-3333")
    assert menor.maior_de_idade is False


def test_fazer_aniversario(cliente):
    cliente.fazer_aniversario()
    assert cliente.idade == 26


def test_idade_negativa_na_criacao_levanta_erro():
    with pytest.raises(ValueError):
        Cliente("João", -5, "99999-1111")


def test_idade_negativa_no_setter_levanta_erro(cliente):
    with pytest.raises(ValueError):
        cliente.idade = -1


def test_estados_independentes():
    c1 = Cliente("João", 25, "99999-1111")
    c2 = Cliente("Carlos", 30, "99999-2222")
    c1.nome = "João Silva"
    assert c2.nome == "Carlos"


def test_atributo_de_classe_compartilhado():
    c1 = Cliente("João", 25, "99999-1111")
    c2 = Cliente("Carlos", 30, "99999-2222")
    assert c1.nome_sistema == c2.nome_sistema == Cliente.nome_sistema