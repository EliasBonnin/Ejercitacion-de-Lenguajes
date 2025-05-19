# Ejercicio 04* Extra
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Variables

var_ref = 5
var_ref2 = 10
var_fun = 0
var_fun2 = 0

# Programa1


def Programa1(var1, var2):
    var2 = var1
    var1 = var2
    return (var1, var2)


var_fun, var_fun2 = Programa1(var_ref, var_ref2)
print(f"Valor Original {var_ref}, {var_ref2}")
print(f"Valor Funcion {var_fun}, {var_fun2}")

# Programa2


def Programa2(var3, var4):
    return
