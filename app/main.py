from presentation.biblioteca_vm import BibliotecaViewModel
from ui.cli import iniciar_interfaz

def main():
    credenciales = 'c:/Users/perso/Desktop/Universidad Esteban/semestre 1/Programacion orientada a objetos/biblioteca_parcial1/biblio-teca-4cc72-firebase-adminsdk-fbsvc-f29e68678b.json'  
    viewmodel = BibliotecaViewModel(credenciales)
    iniciar_interfaz(viewmodel)

if __name__ == "__main__":
    main()