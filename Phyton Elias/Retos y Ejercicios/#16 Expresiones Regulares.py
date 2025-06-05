# Ejercicio 16
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import re


def encontrar_numeros(texto: str) -> list:
    return re.findall(r"\d+", texto)  # Busca si existe uno o mas digitos en un texto


print(encontrar_numeros("El ejercicio de la fecha de hoy 06/06/25"))

# Extra


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))


print(validate_email("elias@gmail.com"))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


print(validate_phone("+54 1554334"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))


print(validate_url("http://www.elias.dev"))
