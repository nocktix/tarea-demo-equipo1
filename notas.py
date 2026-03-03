"""Cálculo de promedios de notas."""


def promedio_ponderado(notas, ponderaciones):
    """Promedio ponderado de `notas` según `ponderaciones` (en porcentaje)."""
    if len(notas) != len(ponderaciones):
        raise ValueError("Debe haber una ponderación por cada nota")
    total = sum(ponderaciones)
    return sum(n * p for n, p in zip(notas, ponderaciones)) / total
