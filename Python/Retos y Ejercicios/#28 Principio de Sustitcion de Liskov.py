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
