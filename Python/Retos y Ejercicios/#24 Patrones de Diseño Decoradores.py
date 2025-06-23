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
