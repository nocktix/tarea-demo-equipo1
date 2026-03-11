"""Validaciones de los datos de entrada."""

NOTA_MINIMA = 1.0
NOTA_MAXIMA = 7.0


def validar_nota(nota):
    """La escala chilena va de 1.0 a 7.0."""
    if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        raise ValueError(f"La nota {nota} está fuera de la escala (de {NOTA_MINIMA} a {NOTA_MAXIMA})")
    return nota


def validar_ponderaciones(ponderaciones):
    """Las ponderaciones deben sumar 100."""
    suma = sum(ponderaciones)
    if abs(suma - 100) > 1e-9:
        raise ValueError(f"Las ponderaciones suman {suma} y deben sumar 100")
    return ponderaciones
