# Ejercicio 18
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Conjuntos (Lista)

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

print(f"el elemento existe? {-1 in conjunto}")

# del conjunto   Esto elimina el objeto entero del programa a tener en cuenta

conjunto.clear()  # Se limpia completamente la estructura de datos

print(conjunto)

# Extra

set_1 = {1, 2, 3, 4, 5, 8}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Union: {set_1.union(set_2)}")

print(f"Interseccion: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simetrica: {set_1.symmetric_difference(set_2)}")
