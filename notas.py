"""Cálculo de promedios de notas."""

import csv


def promedio_ponderado(notas, ponderaciones):
    """Promedio ponderado de `notas` según `ponderaciones` (en porcentaje)."""
    if len(notas) != len(ponderaciones):
        raise ValueError("Debe haber una ponderación por cada nota")
    total = sum(ponderaciones)
    return sum(n * p for n, p in zip(notas, ponderaciones)) / total


def cargar_notas(ruta):
    """Lee un CSV con columnas evaluacion, nota y ponderacion. Devuelve (notas, ponderaciones)."""
    notas, ponderaciones = [], []
    with open(ruta, newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            notas.append(float(fila["nota"]))
            ponderaciones.append(float(fila["ponderacion"]))
    return notas, ponderaciones
