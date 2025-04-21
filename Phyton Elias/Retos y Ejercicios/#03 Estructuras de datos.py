# Ejercicio 03
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Estructuras de control

# Variables
nombre = 'Elias'
edad = 26
localidad = 'Posadas'

# Tipo de Estrctura lista
my_list = [1, 2, 3, 'Hola']

# Tipo de Estrctura set
my_set = [1, 2, 3,]

# Tipo de Estrctura diccionario
my_dic = {'nombre:': nombre, 'edad:': edad, 'localidad': localidad}

# Tipo de estructura tupla
my_tupla = [1, 2, 3]

# Ejecutamos comando sobre las Estructuras

# Tipo List

print(my_list)

my_list.append(4)  # Agrega al final de la lista un elemento.
print(my_list)

my_list.insert(3, 3.5)  # Agrega un elemento a la lista en el lugar especificado
print(my_list)

my_list.remove('Hola')  # Remueve un valor conocido de la lista
print(my_list)

del my_list[0]  # Elimina el primer elemento de la lista
print(my_list)

my_list.pop()  # Eliminamos el ultimo valor de la lista
print(my_list)

my_list[0] = 4  # Actualizamos el valor de la lista asignando otro
print(my_list)

my_list.sort()  # Ordenamos de manera ascenedente
print(my_list)

#  Tipo set

print(my_set)

my_set.append(4)  # Agregamos un valor al set
print(my_set)

my_set.insert(2, 3.5)  # Inserta en una posicion espeficifa un valor
print(my_set)

my_set.remove(4)  # Remueve un valor conocido del set
print(my_set)

del my_set[0]  # Elimina el elemento en el lugar 0 (primero)
print(my_set)
