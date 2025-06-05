# Ejercicio 19
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import requests

respuesta = requests.get("https://google.com")

print(respuesta.text)
