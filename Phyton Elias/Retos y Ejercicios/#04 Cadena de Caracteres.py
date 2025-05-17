# Ejercicio 04
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Variables

v_cadena = "Hola"
v_cadena2 = "Python"
v_cadena3 = "elias bonnin"

# Concatenacion

print(v_cadena + ", " + v_cadena2 + "!")  # Concatenamos cadenas sumandolas, podemos agregar espacios en el medio

# Repeticion

print(v_cadena * 3)  # Repetimos la cantidad de veces de 3 en este caso

# Indexacion

print(v_cadena[0] + v_cadena[1] + v_cadena[2])

# Longitud

print(len(v_cadena2))

# Slicing (Particionar)

print(v_cadena2[2:6])  # Si queremos un slice Concetro

print(v_cadena2[2:])  # Imprime hasta el final si necesidad de decirlo

print(v_cadena2[:2])  # Imprime desde el inicio hasta el indice 2 si necesidad de aclararlo

# Busqueda

print("a" in v_cadena)  # Buscamos si una cadena de caracteres "a" esta contenida en otra cadena "v_cadena"

# Remplazo

print(v_cadena.replace("o", "a"))  # Remplazamos donde estaria la existencia de cadena "o" por una "a"

# Division

print(v_cadena2.split("t"))  # Dividimos en el lugar que eligamos"t" y eliminamos en el proceso el punto elegido

# Conversion Mayusculas y Minusculas y Primera letra Mayuscula

print(v_cadena.upper())  # Pone todo en Mayuscula
print(v_cadena.lower())  # Pone todo en Minuscula
print(v_cadena3.title())  # Pone todos los primeros caracteres en Mayuscula
print(v_cadena3.capitalize())  # Pone solo el PRIMER caracter en Mayuscula

# Eliminacion de espacios al principio y final

v_cadena3 = " elias bonnin "
print(v_cadena3.strip() + "Eliasdev")

# Busqueda a principio y al final

print(v_cadena.startswith("Ho"))  # Podemos ver si la cadena empieza por un determinado texto
print(v_cadena.startswith("Py"))

print(v_cadena.endswith("la"))  # Podemos ver si la cadena termina por un determinado texto

# Busqueda de posicion

print("elias bonnin @hotmail".find("bonnin"))  # Nos dice la Posicion donde esta empezando esa cadena buscada
print("Elias Bonnin @hotmail".lower().find("b"))
