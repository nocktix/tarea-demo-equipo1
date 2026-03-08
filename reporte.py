"""Formato de salida del reporte."""


def formatear_reporte(resumen):
    lineas = [
        "Reporte de notas",
        "----------------",
        f"Cantidad:   {resumen['cantidad']}",
        f"Promedio:   {resumen['promedio']}",
        f"Mediana:    {resumen['mediana']}",
        f"Desviación: {resumen['desviacion']}",
    ]
    return "\n".join(lineas)
