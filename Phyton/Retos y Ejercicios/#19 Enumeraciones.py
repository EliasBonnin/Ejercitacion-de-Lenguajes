# Ejercicio 19
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

from enum import Enum

# Enumeracion


class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def mostrar_dia(numero: int):
    print(Weekday(numero).name)


mostrar_dia(1)
mostrar_dia(2)
mostrar_dia(4)
