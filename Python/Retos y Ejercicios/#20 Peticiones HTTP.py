# Ejercicio 19
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import requests
import time

respuesta = requests.get("https://google.com/")

if respuesta.status_code == 200:
    print(respuesta)
else:
    print(f"No se obtuvo la respuesta exitosa codigo: {respuesta.status_code}")

# Extra


def MostrarMenu():
    print("Busca tu Pokemon")
    print("1. Buscar pokemon")
    print("2. Salir\n")


while True:
    MostrarMenu()

    action = input("Elegir Opcion: ")

    if action == "1":
        pokemon = input("Ingrese el numero o nombre del pokemon: ")
        respuesta = requests.get(f"https://pokeapi.co/api/vs/pokemon/{pokemon}/")
        if respuesta.status_code == 200:
            print(respuesta)
            time.sleep(2)
        else:
            print(f"No se obtuvo la respuesta exitosa codigo: {respuesta.status_code}")
            time.sleep(2)
    elif action == "2":
        break
