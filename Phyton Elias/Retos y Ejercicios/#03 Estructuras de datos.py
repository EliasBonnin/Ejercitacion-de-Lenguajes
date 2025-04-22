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
my_set = {1, 3, 4, 2}

# Tipo de Estrctura diccionario
my_dict: dict = {'nombre:': nombre, 'edad:': edad, 'localidad': localidad}

# Tipo de estructura tupla
my_tupla: tuple = (4, 5, 1, 8)

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

print(f"{my_list}\n")

# Tuplas

print(my_tupla[1])  # Acceso

my_tupla = tuple(sorted(my_tupla))  # Ordenacion

print(f"{my_tupla}\n")

# Sets

my_set.add(6)  # Insercion
print(my_set)

# No se puede insertar el mismo dato, de esta manera podemos serializar de manera mas facil //my_set.add(6)

# Eso no se puede hacer porque no tiene sentido en el Set //print(my_set[0])

my_set.remove(6)  # Borrado

my_set = set(sorted(my_set))  # No se puede ordenar por su naturaleza
print(my_set)


# Diccionario

print(my_dict)

print(my_dict['nombre:'])  # Acceso

my_dict["provincia:"] = 'Misiones'  # Insercion

my_dict['localidad'] = 'Garuhape'  # Actualizacion

del my_dict['edad:']

print(my_dict)
