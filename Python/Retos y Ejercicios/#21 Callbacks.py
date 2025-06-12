# Ejercicio 20
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

def proceso_saludo(nombre: str, callback):
    callback(nombre)


def saludo_callback(nombre: str):
    print(f"Hola, {nombre}!")


proceso_saludo("Elias", saludo_callback)
