#Ejercicio 02

# En el siguiente URL https:/python.org Tenemos la documentacion de phyton y donde podemos ver todas las funciones y metodos que podemos usar en phyton.
 
# Los retos se encuentran en https://retosdeprogramacion.com/ 

#Funciones

parametro = 10

funcion_variable = 0

funcion_variable2 = "string"


def my_funcion ():
    print("Mi funcion sin retorno")

def my_funcion_con_parametro (parametro):
    my_variable = 5
    my_variable = my_variable + parametro
    return parametro


#Llamado a funciones

my_funcion()

variable = my_funcion_con_parametro(parametro)
print(f"Retorno de funcion con parametro {variable}")



