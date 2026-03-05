"""Validaciones de los datos de entrada."""

NOTA_MINIMA = 1.0
NOTA_MAXIMA = 7.0


def validar_nota(nota):
    """La escala chilena va de 1.0 a 7.0."""
    if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        raise ValueError(f"Nota fuera de rango: {nota}")
    return nota


def validar_ponderaciones(ponderaciones):
    """Las ponderaciones deben sumar 100."""
    if abs(sum(ponderaciones) - 100) > 1e-9:
        raise ValueError("Las ponderaciones deben sumar 100")
    return ponderaciones
