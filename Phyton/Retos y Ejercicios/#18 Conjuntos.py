# Ejercicio 18
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Conjuntos

conjunto = [1, 2, 3, 4, 5]

conjunto.append(6)  # Se agrega al final

print(conjunto)

conjunto.insert(0, 0)  # Se agrega al inicio

print(conjunto)

conjunto.extend([7, 8, 9])  # Se agrega al final una estructura de datos

print(conjunto)

conjunto[3:3] = [-1, -2, -3]  # Altura 3 e indice 3 para agregar un elemento en conjunto

print(conjunto)

del conjunto[3]  # Eliminamos un elemento en una posicion concreta

print(conjunto)

conjunto[3] = 3

print(conjunto)

print(f"el elemnto existe? {-1 in conjunto}")

# del conjunto   Esto elimina el objeto entero del programa a tener en cuenta

conjunto.clear()  # Se limpia completamente la estructura de datos

print(conjunto)
