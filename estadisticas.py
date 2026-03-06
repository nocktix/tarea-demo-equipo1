"""Estadísticas básicas de un conjunto de notas."""


def mediana(notas):
    ordenadas = sorted(notas)
    n = len(ordenadas)
    medio = n // 2
    if n % 2:
        return ordenadas[medio]
    return (ordenadas[medio - 1] + ordenadas[medio]) / 2


def desviacion_estandar(notas):
    """Desviación estándar muestral."""
    n = len(notas)
    if n < 2:
        return 0.0
    promedio = sum(notas) / n
    return (sum((x - promedio) ** 2 for x in notas) / (n - 1)) ** 0.5
