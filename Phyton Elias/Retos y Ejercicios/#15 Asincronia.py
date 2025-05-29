# Ejercicio 14
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Asincronia

from datetime import datetime
import time
import asyncio


async def tarea(nombre: str, duracion: int):
    print(f"Tarea: {nombre}, Duracion: {duracion}s, Inicio a {datetime.now()}")
    time.sleep(duracion)
    print(f"Tarea: {nombre}, Fin: {datetime.now()}")

asyncio.run(tarea("1", 2))
asyncio.run(tarea("2", 4))
