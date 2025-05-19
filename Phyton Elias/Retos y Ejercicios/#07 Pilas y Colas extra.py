# Ejercicio 07
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

# Funcion Web PILA

import time


def NavegacionWeb():
    pila = []
    while True:
        action = input("Añade una URL o interactua con las palabras adelante/atras/salir:  ")

        if action == "salir":
            print("Esta saliendo del navegador")
            time.sleep(1)
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(pila) > 0:
                pila.pop()
        else:
            pila.append(action)

        if len(pila) > 0:
            print(f"Has navegado a la web: {pila[len(pila) - 1]}")
        else:
            print("Estas en la pagina de inicio")


# NavegacionWeb()


def Impresorapy():

    cola = []

    while True:

        action = input("Ingrese el documento o interactue con imprimir/salir:  ")

        if action == "salir":
            print("Usted esta saliendo de la impresora")
            time.sleep(1)
            break
        elif action == "imprimir":
            if len(cola) > 0:
                print(f"Se imprime el siguiente archivo: {cola.pop(0)}")
        else:
            cola.append(action)

        print(f"Cola de impresion {cola}")


Impresorapy()
