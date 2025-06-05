# Ejercicio 17
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Iteraciones

def iteracion_for(numero):  # Iteramos con un for
    for i in range(1, numero + 1):
        print(i)


def iteracion_while(numero):  # Iteramos con un while
    i = 1
    while i <= numero:
        print(i)
        i += 1


def contar_10(numero=1):  # Iteramos con recursividad
    if numero <= 10:
        print(numero)
        contar_10(numero + 1)


iteracion_for(10)

iteracion_while(10)

contar_10()


# Extra

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)
