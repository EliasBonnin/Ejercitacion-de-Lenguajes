# Ejercicio 14
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Fechas

from datetime import datetime

fecha_hoy = datetime.now()  # Fecha hoy
fecha_cumple = datetime(1999, 2, 12, 3, 0, 0)  # Fecha cumpleaños
print(fecha_hoy, fecha_cumple)

diferencia = fecha_hoy - fecha_cumple
print(type(diferencia))

print(diferencia.days // 365)

print(f"mi edad es {(diferencia.days // 365)} años")
