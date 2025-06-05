# Ejercicio 19
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import requests

respuesta = requests.get("https://google.com/")

if respuesta.status_code == 200:
    print(respuesta.text)
else:
    print(f"No se obtuvo la respuesta exitosa codigo: {respuesta.status_code}")
