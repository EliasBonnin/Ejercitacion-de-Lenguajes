# Ejercicio 26
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# (OCP)

from abc import ABC, abstractmethod

# Incorrecta


class MalaForma:

    def dibujar_cuadrado(self):
        print("Dibujar un cuadrado")

    def dibujar_circulo(self):
        print("Dibujar un circulo")


# Correcta

class Forma:
    def dibujar(self):
        pass


class Cuadrado(Forma):
    def dibujar(self):
        print("Dibujar un cuadrado")


class Circulo(Forma):
    def dibujar(self):
        print("Dibujar un circulo")

# Extra


class Operacion(ABC):
    @abstractmethod
    def ejecutarse(self, a, b):
        pass


class Suma(Operacion):
    def ejecutarse(self, a, b):
        return a + b


class Resta(Operacion):
    def ejecutarse(self, a, b):
        return a - b


class Multiplicacion(Operacion):
    def ejecutarse(self, a, b):
        return a * b


class Division(Operacion):
    def ejecutarse(self, a, b):
        return a / b


class Potencia(Operacion):
    def ejecutarse(self, a, b):
        return a ** b


class Calculadora:

    def __init__(self):
        self.operaciones = {}

    def add_operaciones(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre not in self.operaciones:
            raise ValueError(f"La operacion {nombre} no esta soportada por el sistema")
        return self.operaciones[nombre].ejecutarse(a, b)


calculador = Calculadora()

calculador.add_operaciones("suma", Suma())
calculador.add_operaciones("resta", Resta())
calculador.add_operaciones("multiplicar", Multiplicacion())
calculador.add_operaciones("division", Division())
calculador.add_operaciones("potencia", Potencia())

print(calculador.calcular("suma", 10, 10))
print(calculador.calcular("resta", 10, 10))
print(calculador.calcular("multiplicar", 10, 10))
print(calculador.calcular("division", 10, 10))
print(calculador.calcular("potencia", 10, 10))
