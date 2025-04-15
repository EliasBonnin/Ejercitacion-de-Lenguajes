#Ejercicio 02

# En el siguiente URL https:/python.org Tenemos la documentacion de phyton y donde podemos ver todas las funciones y metodos que podemos usar en phyton.
 
# Los retos se encuentran en https://retosdeprogramacion.com/ 

#Funciones

my_param = 10
salida_funcion = "str"
salida_funcion2 = 0
salida_funcion3 = 0

funcion_variable = 0
funcion_variable2 = "str"
funcion_variable3 = 5
funcion_variable4 = 12

def my_funcion (): # Funcion sin retorno
    print("Mi funcion sin retorno")

def my_funcion_con_parametro (my_param): # Funcion con retorno
    my_variable = 5
    my_variable = my_variable + my_param
    return my_param

def my_funcion_con_muchos_parametros (param_1, param_2, param_3): # Funcion con muchos parametros
    my_variable1 = 5
    my_variable2 = 10
    my_variable3 = "Muchos Parametros"
    my_variable2 = my_variable1 + param_1 - param_3 / param_2
    return (my_variable2, my_variable3)



#Llamado a funciones

my_funcion() #Llamado a funcion sin retorno

my_variable = my_funcion_con_parametro(my_param) #Llamado a funcion con retorno
print(f"Retorno de funcion con parametro {my_variable}")

salida_funcion, salida_funcion2 = my_funcion_con_muchos_parametros(funcion_variable, funcion_variable3, funcion_variable4)
print(f"Retorno de funcion con muchos parametros {salida_funcion} {salida_funcion2}") #Llamado a funcion con muchos parametros de retorno

# Funciones de phyton

doble = lambda x: x * 2 # Guardamos una "funcion" matematica en este ejemplo para usarla y ser llamada en el futuro
print(doble(4))

sumar = lambda a, b: a + b # Mas de un parametro
sumar_variable = sumar(2, 3) 
print(sumar_variable)

print("funcion print") # Funcion print

print(f"imprimimos el tipo usando type {type(sumar)}") # Funcion Type

print(f"Devolvemos la longitud de la variable usando len = {len(funcion_variable2)}") # Funcion Len

range_list= list(range(1,5))

my_list=list(range(6, 10))

print(f"Generamos un rango de numeros usando range y list {range_list}") # Genera un rango de numeros en una lista

nombres = ['Elias', 'Yoshi', 'Rodri']
edad = [26 , 23, 23]

zip_list = zip(nombres, edad)
print(f"unificamos 2 listas diferentes utilizando zip {list(zip_list)}") # Utilizamos 2 listas distinitas y las unificamos

round_num =  3.3
print(f"Hacemos un redondeo utilizando round  de 3.3 a {round(round_num)}")

abs_num = -4
print(f"Utilizando la funcion abs obtenemos el valor absoluto de un numero de -4 a {abs(abs_num)}") # Utilizamos abs para obtener el absoluto

# Funciones dentro de funciones

var_edad = 26.5

def Array_nombres_edad(edad):
    round_edad = round(edad)
    return round_edad

round_edad_print = Array_nombres_edad(var_edad)

print(round_edad_print)