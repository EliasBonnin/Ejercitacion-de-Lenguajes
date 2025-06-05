# Ejercicio 19
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

from enum import Enum

# Enumeracion


class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7


def mostrar_dia(numero: int):
    print(Weekday(numero).name)


mostrar_dia(1)


# Extra

class Estado_Pedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Pedido:

    estado = Estado_Pedido.PENDIENTE

    def __init__(self, id: int):
        self.id = id

    def enviado(self):
        if self.estado == Estado_Pedido.PENDIENTE:
            self.estado = Estado_Pedido.ENVIADO
            self.mostrar_estado()
        else:
            print(f"El estado del pedido debe ser Pendiente, el estado del pedido actual es {self.estado.name}")

    def entregado(self):
        if self.estado == Estado_Pedido.ENVIADO:
            self.estado = Estado_Pedido.ENTREGADO
            self.mostrar_estado()
        else:
            print(f"El estado del pedido debe ser Enviado, el estado del pedido actual es {self.estado.name}")

    def cancelado(self):
        if self.estado != Estado_Pedido.ENTREGADO:
            self.estado = Estado_Pedido.CANCELADO
            self.mostrar_estado()
        else:
            print("El pedido ya se a entregado, no se puede CANCELAR")

    def mostrar_estado(self):
        print(f"El estado del pedido nro: {self.id} es: {self.estado.name}")


pedido_1 = Pedido(1)

pedido_1.enviado()
pedido_1.entregado()
pedido_1.cancelado()
