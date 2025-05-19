# Ejercicio 07
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

# Pila/Stack (LIFO)

Pila = []

# Push

Pila.append(1)
Pila.append(2)
Pila.append(3)

print(Pila)

# Pop

Pila_item = Pila[len(Pila) - 1]  # Con esto obtenemos el primer item de la pila.
del Pila[len(Pila) - 1]  # Al obtenerlo debemos removerlo del conjnunto de elementos de la pila
print(Pila_item)

print(Pila.pop())  # Remueve el valor mas alto de la pila.

print(Pila)


# Cola/Queue [FIFO]

Cola = []

# Encolar

Cola.append(1)
Cola.append(2)
Cola.append(3)

print(Cola)

# Descolar

Cola_item = Cola[0]
del Cola[0]
print(Cola_item)


print(Cola.pop(0))

print(Cola)
