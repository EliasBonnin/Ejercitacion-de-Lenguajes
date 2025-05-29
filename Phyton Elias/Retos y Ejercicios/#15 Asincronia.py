# Ejercicio 14
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Asincronia

from datetime import datetime
import asyncio


async def tarea(nombre: str, duracion: int):
    print(f"Tarea: {nombre}, Duracion: {duracion}s, Inicio a {datetime.now()}")
    await asyncio.sleep(duracion)
    print(f"Tarea: {nombre}, Fin: {datetime.now()}")

asyncio.run(tarea("1", 2))

# Extra


async def tarea_asincrona():
    await asyncio.gather(tarea("C", 3), tarea("B", 2), tarea("A", 1))
    await tarea("D", 1)

asyncio.run(tarea_asincrona())
