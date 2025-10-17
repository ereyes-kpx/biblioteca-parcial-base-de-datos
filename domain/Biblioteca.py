class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def obtener_libros(self):
        return self.__libros.copy()

    def obtener_usuarios(self):
        return self.__usuarios.copy()