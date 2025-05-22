# Ejercicio 11
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Manejo de Ficheros

import os

nombre_archivo = "EliasBonnin.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("Bonnin Elias\n")
    archivo.write("26\n")
    archivo.write("Python\n")

with open(nombre_archivo, "r") as archivo:
    print(archivo.read())

os.remove(nombre_archivo)


# Limpiar Consola

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Extra


archivo_local = "GestionVentas.txt"
open(archivo_local, "a")


def mostrar_menu():
    print("\n Gestion de Productos")
    print("1. insertar Producto")
    print("2. Actualizar Producto")
    print("3. Buscar Producto")
    print("4. Borrar Producto")
    print("5. Calcular Venta por Producto")
    print("6. Calcular Venta Total")
    print("7. Salir\n")


while True:
    limpiar_consola()
    mostrar_menu()

    action = input("Elegir Opcion:  ")

    if action == "1":
        limpiar_consola()
        nombre = input("Ingrese nombre de producto:  ")
        cantidad = input("Ingrese cantidad vendida:  ")
        precio = input("Ingrese el precio:  ")
        with open(archivo_local, "a") as archivo:
            archivo.write(f"{nombre}, {cantidad}, {precio}")
    elif action == "2":
        pass
    elif action == "3":
        pass
    elif action == "4":
        pass
    elif action == "5":
        pass
    elif action == "6":
        pass
    elif action == "7":
        os.remove(archivo_local)
        break
    else:
        print("Seleccione solo las opciones disponibles")
