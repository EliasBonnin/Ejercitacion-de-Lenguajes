# Ejercicio 25
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# SRP

# Manera Incorrecta

class Usuario:  # Al tener responsabilidad de guardado y email, al cambiar una de ellas afectaria la clase

    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email

    def guardar_usuario(self):
        pass

    def enviar_email(self):
        pass


# Manera Correcta

class Usuarios:

    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email


class UsuarioRepo:

    def guardar_usuario(self, user):
        pass


class EmailServicio:

    def enviar_email(self, email, mensaje):
        pass


# Extra

# Manera incorrecta
class Libreria:

    def __init__(self, ):
        self.libros = []
        self.prestamos = []
        self.usuarios = []

    def registro_libros(self, titulo, autor, copias):
        self.libros.append({"titulo": titulo, "autor": autor, "copias": copias})

    def agregar_usuarios(self, nombre, id, email):
        self.usuarios.append({"nombre": nombre, "id": id, "email": email})

    def alquilar_libro(self, id, titulo):
        for libro in self.libros:
            if libro["titulo"] == libro.titulo and libro["copias"] > 0:
                libro["copias"] -= 1
                self.prestamos.append({"id": id, "titulo": titulo, })
            return True
        return False

    def devolver_libro(self, id, titulo):
        for libro in self.prestamos:
            if libro["id"] == id and libro["titulo"] == titulo:
                self.prestamos.remove(libro)
                for libro in self.libros:
                    if libro["titulo"] == libro.titulo:
                        libro["copias"] += 1
                    return True
            return False


# Manera Correcta

class Libro:

    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias


class User:

    def __init__(self, nombre, id, email):
        self.nombre = nombre
        self.id = id
        self.email = email


class Prestamo:

    def __init__(self):
        self.prestamos = []

    def alquilar_libro(self, user, libro):
        if libro.copias > 0:
            libro.copias -= 1
            self.prestamos.append({"id": user.id, "titulo": libro.titulo})
        return True

    def devolver_libro(self, user, libro):
        for libro in self.prestamos:
            if libro["id"] == user.id and libro["titulo"] == libro.titulo:
                self.prestamos.remove(libro)
                libro.copias += 1
            return True
        return False


class LibreriaCorrecta:

    def __init__(self, ):
        self.libros = []
        self.prestamos = Prestamo()
        self.usuarios = []

    def registro_libros(self, libro):
        self.libros.append(libro)

    def agregar_usuarios(self, user):
        self.usuarios.append(user)

    def alquilar_libro(self, user_id, libro_titulo):
        user = next((i for i in self.users if i.id == user_id), None)
        libro = next((i for i in self.libros if i.id == libro_titulo), None)
        if user and libro:
            return self.prestamos.alquilar_libro(user, libro)
        return False

    def devolver_libro(self, user_id, libro_titulo):
        user = next((i for i in self.users if i.id == user_id), None)
        libro = next((i for i in self.libros if i.id == libro_titulo), None)
        if user and libro:
            return self.prestamos.devolver_libro(user, libro)
        return False
