# Ejercicio 03* Extra
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

import os
import time

# Funciones utiles


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables


op_interfaz = 0  # Variable que usaremos para movernos sobre la interfaz principal
nombre_agenda = "Nombre"  # Nombre del agendado
num_tel = 0  # Numero de Telefono del agendado

# Listas

my_agenda: dict = {}

# Interfaz - Terminal


def mostrar_menu():
    print("\n Agenda de contantos")
    print("1. insertar Contacto")
    print("2. Actualizar Contacto")
    print("3. Buscar Contacto")
    print("4. Borrar Contacto")
    print("5. Mostrar Agenda y Salir\n")


# limpiar_consola()
while True:
    limpiar_consola()
    mostrar_menu()
    op_interfaz = input("Elegir opcion 1-5\n")

    if op_interfaz == "1":
        limpiar_consola()
        print("      Insertar Contacto\n")
        nombre_agenda = input("Ingresa el nombre del usuario \n")
        while True:
            num_tel = input("Ingrese el numero de telefono \n")
            if num_tel.isdigit() and len(num_tel) <= 11:
                my_agenda[nombre_agenda] = num_tel
                print("El contacto se agrego correctamete...\n")
                time.sleep(1)
                break
            else:
                print("El numero debe ser solo numeros y debe tener un maximo de 11 digitos \n")

    elif op_interfaz == "2":
        limpiar_consola()
        print("      Actualizar un contacto\n")
        while True:
            nombre_agenda = input("Ingrese el Nombre del contacto a Actualizar o ingrese 0 para salir \n")
            if nombre_agenda in my_agenda:
                while True:
                    num_tel = input("Ingrese el NUEVO numero de telefono \n")
                    if num_tel.isdigit() and len(num_tel) <= 11:
                        my_agenda[nombre_agenda] = num_tel
                        print("El contacto se actualizo correctamete...\n")
                        time.sleep(1)
                        break
                    else:
                        print("El numero debe ser solo numeros y debe tener un maximo de 11 digitos \n")
                break
            elif nombre_agenda == "0":
                break
            else:
                print("El nombre de contacto no existe, intente nuevamente\n")
    elif op_interfaz == "3":
        limpiar_consola()
        print("         Buscar un contacto")
        while True:
            nombre_agenda = input("Ingrese el Contacto a Buscar o 0 para salir\n")
            if nombre_agenda in my_agenda:
                print(f"El Numero de {nombre_agenda} es: {my_agenda[nombre_agenda]}\n\n")
            elif nombre_agenda == "0":
                break
            else:
                print("El usuario buscado no Existe\n\n")
    elif op_interfaz == "4":
        limpiar_consola()
        print("      Borrar un contacto")
        while True:
            nombre_agenda = input("Ingrese el Nombre del Contacto a Eliminar o Ingrese 0 para Salir\n")
            if nombre_agenda in my_agenda:
                del my_agenda[nombre_agenda]
                print("El Contacto a sido Eliminado Correctamente...\n")
                time.sleep(1)
                break
            elif nombre_agenda == "0":
                break
            else:
                print("El Nombre Ingresado no Existe\n")
    elif op_interfaz == "5":
        print("Hasta Luego\n")
        print(f"Agenda de contactos\n {my_agenda}")
        break
    else:
        print("Opcion no valida")
