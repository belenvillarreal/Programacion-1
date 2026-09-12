# Desafío 59: Herencia y especialización
# LibroDigital y EBook

# Este programa demuestra herencia en varios niveles.
# LibroDigital hereda de Libro y EBook hereda de LibroDigital.
# Además, EBook sobrescribe el método mostrar_informacion().


class Libro:
    """Representa los datos generales de un libro."""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        """Muestra la información básica del libro."""
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)


class LibroDigital(Libro):
    """Representa un libro en formato digital."""

    def __init__(
        self,
        titulo,
        autor,
        isbn,
        formato,
        tamaño_archivo
    ):
        # Inicializar los atributos heredados de Libro
        super().__init__(titulo, autor, isbn)

        # Atributos propios de LibroDigital
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        """Muestra toda la información del libro digital."""
        super().mostrar_informacion()
        print("Formato:", self.formato)
        print("Tamaño del archivo:", self.tamaño_archivo)


class EBook(LibroDigital):
    """Representa un libro digital con enlace de descarga."""

    def __init__(
        self,
        titulo,
        autor,
        isbn,
        formato,
        tamaño_archivo,
        enlace_descarga
    ):
        # Inicializar los atributos heredados de LibroDigital
        super().__init__(
            titulo,
            autor,
            isbn,
            formato,
            tamaño_archivo
        )

        # Atributo propio de EBook
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        """Muestra toda la información del EBook."""
        # Reutilizar el método de LibroDigital
        super().mostrar_informacion()

        # Agregar el dato específico de EBook
        print("Enlace de descarga:", self.enlace_descarga)


def main():
    """Prueba el funcionamiento de las clases."""

    print("Desafío 59: LibroDigital y EBook")
    print()

    # Crear un objeto LibroDigital
    libro_digital = LibroDigital(
        "Introducción a Python",
        "Ana Pérez",
        "9781234567890",
        "PDF",
        "5 MB"
    )

    # Crear un objeto EBook
    ebook = EBook(
        "Programación en Python",
        "Carlos Gómez",
        "9780987654321",
        "EPUB",
        "3 MB",
        "https://ejemplo.com/descarga"
    )

    # Mostrar información utilizando el mismo método
    print("Información del LibroDigital:")
    libro_digital.mostrar_informacion()

    print()

    print("Información del EBook:")
    ebook.mostrar_informacion()


if __name__ == "__main__":
    main()