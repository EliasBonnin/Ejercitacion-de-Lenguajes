# Ejercicio 12
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

import xml.etree.ElementTree as xml
import json
import os

datos = {
    "nombre": "Elias",
    "edad": 26,
    "fecha_nacimiento": "12/02/99",
    "lenguajes_prog": ["Python", "C", "Java"]
}

xml_archivo = "elias.xml"
json_archivo = "elias.json"

# XML


def crear_xml():

    root = xml.Element("data")  # El elemento raiz de donde vamos a crear todo

    for key, value in datos.items():  # De aca generamos los elementos hijos del root
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_archivo)


crear_xml()  # Llamado a la funcion XML

with open(xml_archivo) as fichero:
    print(fichero.read())


# JSON


def create_json():
    with open(json_archivo, "w") as json_data:
        json.dump(datos, json_data)


create_json()  # Llamado a la funcion JSON

with open(json_archivo) as fichero:
    print(fichero.read())


# Extra

# XML


class Datos:

    def __init__(self, nombre, edad, fecha_nacimiento, lenguaje_prog):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguaje_prog = lenguaje_prog


with open(xml_archivo, "r") as fichero_xml:
    root = xml.fromstring(fichero_xml.read())
    nombre = root.find("nombre").text
    edad = root.find("edad").text
    fecha_nacimiento = root.find("fecha_nacimiento").text
    lenguajes_prog = []
    for item in root.find("lenguajes_prog"):
        lenguajes_prog.append(item.text)

datos_de_xml = Datos(nombre, edad, fecha_nacimiento, lenguajes_prog)
print(datos_de_xml.__dict__)


# JSON

with open(json_archivo, "r") as fichero_json:
    datas_json = json.load(fichero_json)
    nombre = datas_json["nombre"]
    edad = datas_json["edad"]
    fecha_nacimiento = datas_json["fecha_nacimiento"]
    lenguajes_prog = datas_json["lenguajes_prog"]
    datos_de_json = Datos(nombre, edad, fecha_nacimiento, lenguajes_prog)

print(datos_de_json.__dict__)

os.remove(xml_archivo)
os.remove(json_archivo)
