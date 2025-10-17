from domain.Libro import Libro
from domain.Usuario import Usuario

def mostrar_menu():
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

def iniciar_interfaz(viewmodel):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            viewmodel.registrar_libro(libro)
            print(f"\nLibro '{titulo}' registrado exitosamente.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            viewmodel.registrar_usuario(usuario)
            print(f"\nUsuario '{nombre}' registrado exitosamente.")

        elif opcion == "3":
            libros = viewmodel.listar_libros()
            if not libros:
                print("\nNo hay libros registrados.")
            else:
                print("\nLibros registrados:")
                for libro in libros:
                    print(libro)

        elif opcion == "4":
            usuarios = viewmodel.listar_usuarios()
            if not usuarios:
                print("\nNo hay usuarios registrados.")
            else:
                print("\nUsuarios registrados:")
                for usuario in usuarios:
                    print(usuario)

        elif opcion == "5":
            titulo = input("Ingrese el título del libro a buscar: ")
            resultados = viewmodel.buscar_libro_por_titulo(titulo)
            if resultados:
                print(f"\nResultados para '{titulo}':")
                for libro in resultados:
                    print(libro)
            else:
                print(f"\nNo se encontró ningún libro con el título '{titulo}'.")

        elif opcion == "6":
            print("Saliendo... ¡Gracias por usar la biblioteca!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")