from bibliotecaVirtual import *

def main():
    biblioteca = BibliotecaVirtual()

    while True:
        print("\n--- Biblioteca Virtual Universidad Distrital ---")
        print("1. Mostrar biblioteca")
        print("2. Pedir prestado un libro")
        print("3. Devolver un libro")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            biblioteca.mostrar_biblioteca()
        elif opcion == "2":
            titulo = input("Ingresa el título del libro que deseas pedir prestado: ")
            tipo_usuario = input("Eres '1' (estudiante) o '2' (profesor): ")
            biblioteca.pedir_libro(titulo, tipo_usuario)
        elif opcion == "3":
            titulo = input("Ingresa el título del libro que deseas devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "4":
            biblioteca.guardar_en_archivo("biblioteca.txt")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()