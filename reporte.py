"""Formato de salida del reporte."""


def formatear_reporte(resumen):
    lineas = [
        "Reporte de notas",
        "----------------",
        f"Cantidad:   {resumen['cantidad']}",
        f"Promedio:   {resumen['promedio']:.1f}",
        f"Mediana:    {resumen['mediana']}",
        f"Desviación estándar: {resumen['desviacion']:.2f}",
    ]
    return "\n".join(lineas)
