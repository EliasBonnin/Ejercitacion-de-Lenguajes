# Ejercicio 28
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# PdS

# Forma incorrecta
class Aves:

    def vuelo(self):
        return "volar"


class Pollo(Aves):

    def vuelo(self):
        raise Exception("Los pollos no vuelan")


# pajaro = Aves
# pajaro.vuelo()
# pollito = Pollo
# pollito.vuelo()

class Ave:
    def move(self):
        print("Mueve")


class Chicken(Ave):

    def move(self):
        return print("Camina")


pajaro = Ave()
pajaro.move()
pollito = Chicken()
pollito.move()

# Extra


class Vehiculo:

    def __init__(self, velocidad=0):
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad:  {self.velocidad} Km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad <= 0:
            self.velocidad = 0
        print(f"Velocidad:  {self.velocidad} Km/h")


class Auto(Vehiculo):
    def acelerar(self, incremento):
        print("El Auto esta acelerando")
        super().acelerar(incremento)

    def frenar(self, decremento):
        print("El Auto esta frenando")
        super().frenar(decremento)


class Moto(Vehiculo):

    def acelerar(self, incremento):
        print("La moto esta acelerando")
        super().acelerar(incremento)

    def frenar(self, decremento):
        print("La moto esta frenando")
        super().frenar(decremento)


class Bicicleta(Vehiculo):
    def acelerar(self, incremento):
        print("La bicicleta esta acelerando")
        super().acelerar(incremento)

    def frenar(self, decremento):
        print("La bicicleta esta frenando")
        super().frenar(decremento)


def test_vehiculo(vehiculo):
    vehiculo.acelerar(10)
    vehiculo.frenar(5)


auto = Auto()
bici = Bicicleta()
moto = Moto()

test_vehiculo(auto)
test_vehiculo(bici)
test_vehiculo(moto)
