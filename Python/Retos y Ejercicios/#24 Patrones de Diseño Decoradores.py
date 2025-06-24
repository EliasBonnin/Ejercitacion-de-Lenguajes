# Ejercicio 24
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Decoradores

def imprimir_funcion(funcion):
    def print_funcion():
        print(f"La funcion {funcion.__name__} ha sido llamada")
        return funcion
    return print_funcion


@imprimir_funcion
def ejemplo_funcion():
    pass


@imprimir_funcion
def ejemplo_funcion2():
    pass


@imprimir_funcion
def ejemplo_funcion3():
    pass


ejemplo_funcion()
ejemplo_funcion2()
ejemplo_funcion3()


# Extra

def contador_llamadas(funcion):
    def contar():
        contar.contador_fun += 1
        print(f"La funcion {funcion.__name__} se llamo {contar.contador_fun} vez/veces")
        return funcion

    contar.contador_fun = 0
    return contar


@contador_llamadas
def ejemplo_funcion4():
    pass


@contador_llamadas
def ejemplo_funcion5():
    pass


@contador_llamadas
def ejemplo_funcion6():
    pass


ejemplo_funcion4()
ejemplo_funcion4()
ejemplo_funcion4()
ejemplo_funcion5()
ejemplo_funcion5()
ejemplo_funcion6()
