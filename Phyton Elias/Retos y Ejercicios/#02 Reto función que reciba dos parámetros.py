# Ejercicio 02* Extra
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Variables

var_char = 'Multiplo de 3'
var_char2 = 'Multiplo de 5'


def funcion_ejercicio(parametro1, parametro2) -> int:
    cont = 0
    concatenado = parametro1 + ' y ' + parametro2
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} es {concatenado}")
        elif i % 5 == 0:
            print(f"{i}, es {parametro2}")
        elif i % 3 == 0:
            print(f"{i}, es {parametro1}")
        else:
            print(i)
            cont += 1
    return cont


print(funcion_ejercicio(var_char, var_char2))
