# Ejercicio 11
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Manejo de Ficheros

import os
import time

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
    print("Gestion de Productos")
    print("1. insertar Producto")
    print("2. Actualizar Producto")
    print("3. Buscar Producto")
    print("4. Borrar Producto")
    print("5. Mostrar Productos")
    print("6. Calcular Venta por Producto")
    print("7. Calcular Venta Total")
    print("8. Salir\n")


while True:
    mostrar_menu()

    action = input("Elegir Opcion:  ")

    if action == "1":
        nombre = input("Ingrese nombre de producto:  ")
        cantidad = input("Ingrese cantidad vendida:  ")
        precio = input("Ingrese el precio:  ")
        with open(archivo_local, "a") as archivo:
            archivo.write(f"{nombre}, {cantidad}, {precio}")
    elif action == "2":
        nombre = input("Ingrese nombre de producto:  ")
        cantidad = input("Ingrese cantidad vendida:  ")
        precio = input("Ingrese el precio:  ")
        with open(archivo_local, "w") as archivo:
            for line in archivo.readlines():
                if line.split(", ")[0] == nombre:
                    archivo.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    archivo.write(line)
    elif action == "3":
        nombre = input("Ingresas nombre: ")
        with open(archivo_local, "r") as archivo:
            for line in archivo.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
                    time.sleep(1)
                    break
    elif action == "4":
        nombre = input("Ingresas nombre: ")
        with open(archivo_local, "r") as archivo:
            lines = archivo.readlines()
        with open(archivo_local, "w") as archivo:
            for line in lines:
                if line.split(", ")[0] != nombre:
                    archivo.write(line)
    elif action == "5":
        with open(archivo_local, "r") as archivo:
            print(archivo.read())
            time.sleep(1)
    elif action == "6":
        total = 0
        with open(archivo_local, "r") as archivo:
            for line in archivo.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif action == "7":
        name = input("Nombre: ")
        total = 0
        with open(archivo_local, "r") as archivo:
            for line in archivo.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
    elif action == "8":
        os.remove(archivo_local)
        break
    else:
        print("Seleccione solo las opciones disponibles")
