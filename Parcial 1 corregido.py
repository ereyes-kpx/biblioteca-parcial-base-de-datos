#Autor: Samuel Esteban Reyes Uribe


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"{self.__titulo} - {self.__autor} (ISBN: {self.__isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id_usuario = id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_id_usuario(self):
        return self.__id_usuario

    def __str__(self):
        return f"Usuario: {self.__nombre} (ID: {self.__id_usuario})"


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []

    def registrar_libro(self, libro):
        self.__libros.append(libro)
        print(f"\nLibro '{libro.get_titulo()}' registrado exitosamente.")

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print(f"\nUsuario '{usuario.get_nombre()}' registrado exitosamente.")

    def listar_libros(self):
        if not self.__libros:
            print("\nNo hay libros registrados.")
        else:
            print("\nLibros registrados:")
            for libro in self.__libros:
                print(libro)

    def listar_usuarios(self):
        if not self.__usuarios:
            print("\nNo hay usuarios registrados.")
        else:
            print("\nUsuarios registrados:")
            for usuario in self.__usuarios:
                print(usuario)

    def buscar_libro_por_titulo(self, titulo):
        encontrados = [libro for libro in self.__libros if libro.get_titulo().lower() == titulo.lower()]
        if encontrados:
            print(f"\nResultados para '{titulo}':")
            for libro in encontrados:
                print(libro)
        else:
            print(f"\nNo se encontró ningún libro con el título '{titulo}'.")


def menu():
    print("""
========== Biblioteca ===========
|    1. Registrar libro         |
|    2. Registrar usuario       |
|    3. Listar libros           |
|    4. Listar usuarios         |
|    5. Buscar libro por título |
|    6. Salir                   |
=================================
""")


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.registrar_libro(libro)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "3":
            biblioteca.listar_libros()

        elif opcion == "4":
            biblioteca.listar_usuarios()

        elif opcion == "5":
            titulo_buscar = input("Ingrese el título del libro a buscar: ")
            biblioteca.buscar_libro_por_titulo(titulo_buscar)

        elif opcion == "6":
            print("Saliendo... ¡Gracias por usar la biblioteca!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
    




