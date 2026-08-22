# Desafío 48: Relación entre las clases Libro y Autor

# Este programa crea las clases Autor y Libro.
# Cada libro tiene un título, género, ISBN y un autor.
# Al crear un libro, se agrega automáticamente
# a la lista de libros de su autor.


class Autor:
    """Representa a un autor y los libros que ha escrito."""

    def __init__(self, nombre):
        """Inicializa el nombre del autor y su lista de libros."""
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro a la lista del autor."""
        if libro not in self.libros:
            self.libros.append(libro)

    def eliminar_libro(self, libro):
        """Elimina un libro de la lista del autor si existe."""
        if libro in self.libros:
            self.libros.remove(libro)

    def mostrar_libros(self):
        """Muestra los libros escritos por el autor."""
        print()
        print("Libros de", self.nombre + ":")

        if len(self.libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print("-", libro.titulo)


class Libro:
    """Representa un libro y sus datos principales."""

    def __init__(self, titulo, genero, isbn, autor):
        """Inicializa los datos del libro."""
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

        # Relacionar automáticamente el libro con su autor
        autor.agregar_libro(self)

    def mostrar_informacion(self):
        """Muestra la información del libro."""
        print()
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("ISBN:", self.isbn)
        print("Autor:", self.autor.nombre)


def main():
    """Prueba la relación entre Autor y Libro."""

    print("Desafío 48: Clase Libro y relación con Autor")

    # Crear un autor
    autor = Autor("Gabriel García Márquez")

    # Crear libros relacionados con el autor
    libro_1 = Libro(
        "Cien años de soledad",
        "Novela",
        "9780307474728",
        autor
    )

    libro_2 = Libro(
        "El amor en los tiempos del cólera",
        "Novela",
        "9780307389732",
        autor
    )

    # Mostrar la información de los libros
    libro_1.mostrar_informacion()
    libro_2.mostrar_informacion()

    # Mostrar los libros relacionados con el autor
    autor.mostrar_libros()


# Ejecutar el programa
if __name__ == "__main__":
    main()