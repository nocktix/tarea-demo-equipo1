"""Punto de entrada: python main.py archivo.csv"""

import sys

from estadisticas import resumen
from notas import cargar_notas, promedio_ponderado
from reporte import formatear_reporte
from validaciones import validar_nota, validar_ponderaciones


def main(ruta):
    notas, ponderaciones = cargar_notas(ruta)
    for nota in notas:
        validar_nota(nota)
    validar_ponderaciones(ponderaciones)
    datos = resumen(notas)
    datos["promedio"] = promedio_ponderado(notas, ponderaciones)
    print(formatear_reporte(datos))


if __name__ == "__main__":
    main(sys.argv[1])
