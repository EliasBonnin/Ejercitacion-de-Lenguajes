# Ejercicio 04* Extra
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Variables

var_ref = 5
var_ref2 = 10
var_fun = 0
var_fun2 = 0

list_ref = [1, 2, 3]
list_ref2 = [1, 2, 3, 4]
list_fun = 0
list_fun2 = 0

# Programa1


def Programa1(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return (var1, var2)


var_fun, var_fun2 = Programa1(var_ref, var_ref2)
print(f"Valor Original {var_ref}, {var_ref2}")
print(f"Valor Funcion {var_fun}, {var_fun2} \n")

# Programa2


def Programa2(var3, var4):
    temp = var3
    var3 = var4
    var4 = temp
    return (var3, var4)


list_fun, list_fun2 = Programa2(list_ref, list_ref2)
print(f"Referencia Original {list_ref}, {list_ref2}")
print(f"Referencia Funcion {list_fun}, {list_fun2}")
