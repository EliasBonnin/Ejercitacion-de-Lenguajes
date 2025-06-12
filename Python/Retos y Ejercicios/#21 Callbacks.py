# Ejercicio 21
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import random
import time


def proceso_saludo(nombre: str, callback):
    callback(nombre)


def saludo_callback(nombre: str):
    print(f"Hola, {nombre}!")


proceso_saludo("Elias", saludo_callback)


# Extra

def procesar_pedido(nombre_comida: str, confirmar_callback, terminado_callback, enviado_callback):
    confirmar_callback(nombre_comida)
    time.sleep(random.randint(1, 10))
    terminado_callback(nombre_comida)
    time.sleep(random.randint(1, 10))
    enviado_callback(nombre_comida)


def proceso_confirmar(nombre_comida: str):
    print(f"Tu pedido {nombre_comida} a sido confirmado")


def pedido_terminado(nombre_comida: str,):
    print(f"Tu pedido {nombre_comida} esta listo")


def pedido_enviado(nombre_comida: str,):
    print(f"Tu pedido {nombre_comida} a sido enviado")


procesar_pedido("Pizza triple queso", proceso_confirmar, pedido_terminado, pedido_enviado)
