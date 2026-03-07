import pytest

from validaciones import validar_nota, validar_ponderaciones


def test_nota_valida():
    assert validar_nota(5.5) == 5.5


def test_nota_fuera_de_rango():
    with pytest.raises(ValueError):
        validar_nota(7.5)


def test_ponderaciones_deben_sumar_100():
    assert validar_ponderaciones([50, 50]) == [50, 50]
    with pytest.raises(ValueError):
        validar_ponderaciones([50, 40])
