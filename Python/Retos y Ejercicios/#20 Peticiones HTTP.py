# Ejercicio 20
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
    print("\nBusca tu Pokemon")
    print("1. Buscar pokemon")
    print("2. Salir\n")


while True:
    MostrarMenu()

    action = input("Elegir Opcion: ")

    if action == "1":
        pokemon = input("Ingrese el numero o nombre del pokemon: ").lower()
        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print("\nPokemon Encontrado!!")
            print(f"Nombre: {datos["name"]}")
            print(f"ID: {datos["id"]}")
            print(f"Peso: {datos["weight"]}")
            print(f"Altura: {datos["height"]}")
            print("Tipo(s):")
            for tipo in datos["types"]:
                print(tipo["type"]["name"])
            print("Juegos!")
            for juego in datos["game_indices"]:
                print(juego["version"]["name"])

            respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
            if respuesta.status_code == 200:
                url = respuesta.json()["evolution_chain"]["url"]
                respuesta = requests.get(url)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    print("Cadena de evolucion: ")

                    def get_evoluciones(datos):
                        print(datos["species"]["name"])
                        if "evolves_to" in datos:
                            for evolucion in datos["evolves_to"]:
                                get_evoluciones(evolucion)

                    get_evoluciones(datos["chain"])

                else:
                    print(f"No se obtuvo la respuesta exitosa a evoluciones codigo: {respuesta.status_code}")
            else:
                print(f"No se obtuvo la respuesta exitosa a evoluciones codigo: {respuesta.status_code}")

            time.sleep(3)
        else:
            print(f"No se obtuvo la respuesta exitosa codigo: {respuesta.status_code}")
            time.sleep(2)
    elif action == "2":
        break
