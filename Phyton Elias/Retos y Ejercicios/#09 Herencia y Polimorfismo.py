# Ejercicio 09
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

# SuperClase

class Animal:

    def __init__(self, nombre: str):
        self.nombre = nombre

    def sonido(self):
        pass


# SubClases

class Perro(Animal):

    def sonido(self):
        print("Guau")


class Gato(Animal):

    def sonido(self):
        print("Miau")


def sonido_animal(Animal: Animal):
    Animal.sonido()


mi_animal = Animal(Animal)
sonido_animal(mi_animal)
mi_perro = Perro("Perro")
mi_gato = Gato("Gatito")
sonido_animal(mi_gato)
sonido_animal(mi_perro)

# Extra


class Empleado:
    def __init__(self, identificador: int, nombre: str):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []

    def nuevo(self, item):
        self.empleados.append(item)

    def mostrar_empleados(self):
        for item in self.empleados:
            print(item.nombre)


class Gerente(Empleado):
    def coordinador(self):
        print(f"El empleado {self.nombre}, esta coordinardo el desarrollo")


class GerenteDP(Empleado):
    def __init__(self, identificador, nombre, proyecto: str):
        super().__init__(identificador, nombre)
        self.proyecto = proyecto

    def proyecto_GDP(self):
        print(f"El GDP: {self.nombre}, esta coordinado su proyecto")


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje: str):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def codigo(self):
        print(f"El programador {self.nombre}, esta programando en el lenguaje {self.lenguaje}")

    def nuevo(self, empleado: Empleado):
        print(f"Un programador no tiene empleados a su cargo. {empleado.nombre}, no se aniade")


mi_gerente = Gerente(1, "Eliasdev")
mi_GDP = GerenteDP(2, "Rodri", "PR1")
mi_GDP2 = GerenteDP(3, "Yoshi", "PR2")
mi_prog = Programador(4, "Emma", "Python")
mi_prog2 = Programador(5, "Sergio", "ZCode")
mi_prog3 = Programador(6, "Ale", "Apache")

mi_gerente.nuevo(mi_GDP)
mi_gerente.nuevo(mi_GDP2)

mi_GDP.nuevo(mi_prog)
mi_GDP2.nuevo(mi_prog2)

mi_prog3.nuevo(mi_prog2)

mi_prog.codigo()
mi_GDP.proyecto_GDP()
mi_gerente.coordinador()
mi_GDP.mostrar_empleados()
mi_gerente.mostrar_empleados()
mi_prog.mostrar_empleados()
