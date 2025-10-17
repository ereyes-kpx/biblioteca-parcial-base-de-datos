import firebase_admin
from firebase_admin import credentials, firestore
from domain.Libro import Libro
from domain.Usuario import Usuario
from domain.Biblioteca import Biblioteca


class BibliotecaViewModel:
    def __init__(self, credenciales_path: str):
        
        cred = credentials.Certificate(credenciales_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        
        self.biblioteca = Biblioteca()

    def registrar_libro(self, libro: Libro):
        
        doc_ref = self.db.collection('libros').document(libro.get_isbn())
        doc_ref.set({
            'titulo': libro.get_titulo(),
            'autor': libro.get_autor(),
            'isbn': libro.get_isbn()
        })
        
        self.biblioteca.agregar_libro(libro)

    def registrar_usuario(self, usuario: Usuario):
        doc_ref = self.db.collection('usuarios').document(usuario.get_id_usuario())
        doc_ref.set({
            'nombre': usuario.get_nombre(),
            'id_usuario': usuario.get_id_usuario()
        })
        self.biblioteca.agregar_usuario(usuario)

    def listar_libros(self):
        docs = self.db.collection('libros').stream()
        libros = []
        for doc in docs:
            data = doc.to_dict()
            libro = Libro(data['titulo'], data['autor'], data['isbn'])
            libros.append(libro)
        return libros

    def listar_usuarios(self):
        docs = self.db.collection('usuarios').stream()
        usuarios = []
        for doc in docs:
            data = doc.to_dict()
            usuario = Usuario(data['nombre'], data['id_usuario'])
            usuarios.append(usuario)
        return usuarios

    def buscar_libro_por_titulo(self, titulo):
        libros = []
        query = self.db.collection('libros').where('titulo', '==', titulo).stream()
        for doc in query:
            data = doc.to_dict()
            libro = Libro(data['titulo'], data['autor'], data['isbn'])
            libros.append(libro)
        return libros
