# Ejercicio 06
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

Numero = 100


def Conteo_Numero(valor):
    if valor < 0 or valor == 0:
        print("Termina la recursividad en ", valor)
    else:
        print(valor)
        Conteo_Numero(valor - 1)


Conteo_Numero(Numero)
