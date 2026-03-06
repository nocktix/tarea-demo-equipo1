from estadisticas import desviacion_estandar, mediana


def test_mediana_impar():
    assert mediana([3, 1, 2]) == 2


def test_mediana_par():
    assert mediana([1, 2, 3, 4]) == 2.5


def test_desviacion_de_valores_iguales():
    assert desviacion_estandar([5, 5, 5]) == 0
