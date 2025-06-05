# Ejercicio 16
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import re


def encontrar_numeros(texto: str) -> list:
    return re.findall(r"\d+", texto)


print(encontrar_numeros("El ejercicio de la fecha de hoy 06/06/25"))
