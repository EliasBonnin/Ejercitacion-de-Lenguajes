# Hola mundo Python

print("Hola, Phython")

# Declarando variables

my_string = "Esto es una cadena de texto"
print(my_string)
print(type(my_string))

my_string = 6  # Tipado dinamico
print(type(my_string))
print(my_string)

my_int = 7
my_int = my_int + 4
print(my_int)
# Esto no cambia el valor de la variable, sino del valor en el print
print(my_int - 1)

my_float = 3.14
print(type(my_float))
print(my_float)

# Podemos operar con float e int de manera indistinta
print(my_float + my_int)

my_boole = False
print(type(my_boole))
print(my_boole)

# Para concatenar cadenas de texto, es necesario convertirlos a string
print("El valor de mi entero es " + str(my_int) +
      " y el de mi bool es " + str(my_boole))

# Otra forma de concatenar cadenas de texto y otros tipos de datos
# Usando f-strings, que son una forma mas moderna y legible de hacerlo
print(f"El valor de mi entero es {my_int} y el de mi bool es {my_boole}")

my_list = [my_string, my_int, my_float, my_boole]  # Listas en Python
print(my_list)
print(type(my_list))

print(my_list[0])  # Accediendo a un elemento de la lista

my_dict = {"int: ": my_int, "float: ": my_float,
           "bool: ": my_boole}  # Diccionarios en Python
print(type(my_dict))
print(my_dict)
print(my_dict["int: "])  # Accediendo a un elemento del diccionario


my_set = (my_string, my_int, my_float, my_boole)  # Set en Python
print(type(my_set))
print(my_set)
print(my_set[0])  # Accediendo a un elemento de la Set

my_tuple = (my_string, my_int, my_float, my_boole)  # Tuplas en Python
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])  # Accediendo a un elemento de la Tupla
print(my_tuple[0:2])  # Accediendo a un rango de elementos de la Tupla

# Control de flujos

if my_int == 11 or my_boole is True:  # Estructura de control IF
    print("El valor de mi entero es 11")
elif my_int == 10:
    print("El valor de mi entero es 10")
else:
    print("El valor de mi entero no es 11")

for my_item in my_list:  # Estructura de control FOR
    print(my_item)


def my_function():
    print("Hola desde la funcion")


def my_function_with_return(param):
    return 10 + param  # La funcion devuelve el valor de la suma de 10 + param


my_return = my_function_with_return(5)  # Llamando a la funcion con return
print(my_return)

for my_item in range(10):
    my_function()  # Llamando a la funcion


# Crear una clase

class MyClass:
    my_name: str = "Elias"
    my_age: int = 20

    def __init__(self):
        self.my_name = "Elias"
        self.my_age = 20


my_clase = MyClass()  # Instanciando la clase
print(my_clase.my_name)
print(my_clase.my_age)
