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


def guardado_xml():

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


guardado_xml()  # Llamado a la funcion XML

with open(xml_archivo) as fichero:
    print(fichero.read())

os.remove(xml_archivo)


# JSON

with open(json_archivo, "w") as json_data:
    json.dump(datos, json_data)

with open(json_archivo) as fichero:
    print(fichero.read())

os.remove(json_archivo)
