from notas import promedio_ponderado


def test_promedio_simple():
    assert promedio_ponderado([6.0, 4.0], [50, 50]) == 5.0


def test_promedio_con_ponderaciones_distintas():
    assert round(promedio_ponderado([7.0, 4.0], [75, 25]), 2) == 6.25
