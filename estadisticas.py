"""Estadísticas básicas de un conjunto de notas."""


def mediana(notas):
    ordenadas = sorted(notas)
    n = len(ordenadas)
    medio = n // 2
    if n % 2:
        return ordenadas[medio]
    return (ordenadas[medio - 1] + ordenadas[medio]) / 2
