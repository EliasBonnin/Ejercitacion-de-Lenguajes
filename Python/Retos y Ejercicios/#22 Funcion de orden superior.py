# Ejercicio 22
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Funcion como argumento

from functools import reduce
from datetime import datetime


def superior_funcion(func, x):
    return func(x)


x = superior_funcion(len, "Elias")

print(x)

# Funcion como retorno


def app_multiplicador(x):
    def multiplicador(n):
        return x * n
    return multiplicador


multiplicador = app_multiplicador(2)
print(multiplicador(5))
print(app_multiplicador(2)(6))

# Sistema

numbers = [1, 3, 2, 5, 6]

# map()


def app_doble(n):
    return n * 2


x = list(map(app_doble, numbers))

print(x)


# filter()

def es_dos(n):
    return n % 2 == 0


print(list(filter(es_dos, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def app_sum(x, y):
    return x + y


print(reduce(app_sum, numbers))


# Extra

estudiantes = [
    {"nombre": "Elias", "Nacimiento": "12-02-1999", "Grados": [5, 8, 5, 3, 10]},
    {"nombre": "Carlos", "Nacimiento": "23-02-1979", "Grados": [6, 2, 4, 6, 8]},
    {"nombre": "Javito", "Nacimiento": "18-02-1989", "Grados": [7, 4, 2, 5, 9]},
    {"nombre": "Eljavo", "Nacimiento": "18-02-1989", "Grados": [8, 9, 10, 10, 9]}
]


def media(notas):
    return sum(notas) / len(notas)


print(list(map
           (lambda estudiante:
            {"nombre": estudiante["nombre"],
             "Grados": media(estudiante["Grados"])}, estudiantes)))


# Mejores

print(
    list(
        map(lambda estudiante:
            estudiante["nombre"],
            filter(lambda estudiante: media(estudiante["Grados"]) >= 9, estudiantes)
            )
    )
)

# Nacimiento Ordenado desde el mas joven

print(sorted(estudiantes, key=lambda estudiante: datetime.strptime(
    estudiante["Nacimiento"], "%d-%m-%Y"), reverse=True))


# Calificacion mas alta

print(max(map(lambda estudiante: max(estudiante["Grados"]), estudiantes)))
