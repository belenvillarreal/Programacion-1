# Desafío 47: Clase Autor con lista de libros

# Este programa define una clase Autor que almacena el nombre
# del autor y una lista con los libros escritos por él.
# También incluye métodos para agregar y eliminar libros.


class Autor:
    """Representa a un autor y los libros que ha escrito."""

    def __init__(self, nombre):
        """Inicializa el nombre del autor y su lista de libros."""
        self.nombre = nombre

        # Crear una lista vacía para almacenar los libros del autor
        self.libros = []

    def agregar_libro(self, titulo):
        """Agrega un libro a la lista si todavía no existe."""
        if titulo not in self.libros:
            self.libros.append(titulo)
            print("Libro agregado:", titulo)
        else:
            print("El libro ya se encuentra en la lista:", titulo)

    def eliminar_libro(self, titulo):
        """Elimina un libro de la lista si existe."""
        if titulo in self.libros:
            self.libros.remove(titulo)
            print("Libro eliminado:", titulo)
        else:
            print("No se encontró el libro:", titulo)

    def mostrar_libros(self):
        """Muestra todos los libros registrados del autor."""
        print()
        print("Libros escritos por", self.nombre + ":")

        if len(self.libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print("-", libro)


def main():
    """Prueba el funcionamiento de la clase Autor."""

    print("Desafío 47: Clase Autor")
    print()

    # Crear un objeto de la clase Autor
    autor = Autor("Gabriel García Márquez")

    # Agregar varios libros
    autor.agregar_libro("Cien años de soledad")
    autor.agregar_libro("El amor en los tiempos del cólera")
    autor.agregar_libro("Crónica de una muerte anunciada")

    # Mostrar los libros agregados
    autor.mostrar_libros()

    print()

    # Eliminar uno de los libros
    autor.eliminar_libro("Crónica de una muerte anunciada")

    # Probar el manejo de un libro inexistente
    autor.eliminar_libro("Libro inexistente")

    # Mostrar nuevamente la lista
    autor.mostrar_libros()


# Ejecutar el programa
if __name__ == "__main__":
    main()