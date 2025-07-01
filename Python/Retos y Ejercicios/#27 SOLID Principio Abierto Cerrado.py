# Ejercicio 26
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# (OCP)

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
