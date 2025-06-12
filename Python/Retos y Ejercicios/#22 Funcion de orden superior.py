# Ejercicio 22
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Funcion como argumento

from functools import reduce


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
