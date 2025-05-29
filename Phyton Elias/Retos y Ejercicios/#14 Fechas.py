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

# Extra

# Dia, mes año

print(fecha_cumple.strftime("%d/%m/%y"))
print(fecha_cumple.strftime("%d/%m/%Y"))

# Horas, minutos, segundos

print(fecha_cumple.strftime("%H:%M:%S"))

# Dia del año

print(fecha_cumple.strftime("%j"))

# Dia de a semana

print(fecha_cumple.strftime("%A"))

# Nombre del mes

print(fecha_cumple.strftime("%B"))

# Representacion por defecto del local

print(fecha_cumple.strftime("%c"))
print(fecha_cumple.strftime("%x"))
print(fecha_cumple.strftime("%X"))

# AM/PM

print(fecha_cumple.strftime("%p"))
