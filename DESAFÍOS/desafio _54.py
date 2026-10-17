# Desafío 54: Encapsulamiento con @property

# Este programa implementa la clase Autor utilizando encapsulamiento.
# Los atributos nombre y nacionalidad son privados y se accede a ellos
# mediante propiedades. Los setters validan que no se ingresen
# cadenas vacías.


class Autor:
    """Representa a un autor con nombre y nacionalidad."""

    def __init__(self, nombre, nacionalidad):
        # Los valores se asignan utilizando los setters
        # para que sean validados desde el momento de la creación.
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    @property
    def nombre(self):
        """Devuelve el nombre del autor."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Modifica el nombre si el valor ingresado es válido."""
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede ser una cadena vacía.")

        self._nombre = nuevo_nombre.strip()

    @property
    def nacionalidad(self):
        """Devuelve la nacionalidad del autor."""
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        """Modifica la nacionalidad si el valor ingresado es válido."""
        if (
            not isinstance(nueva_nacionalidad, str)
            or not nueva_nacionalidad.strip()
        ):
            raise ValueError(
                "La nacionalidad no puede ser una cadena vacía."
            )

        self._nacionalidad = nueva_nacionalidad.strip()


def main():
    """Demuestra el funcionamiento de la clase Autor."""

    print("Desafío 54: Encapsulamiento con @property")
    print()

    # 1. Crear un objeto Autor
    autor = Autor("Gabriel García Márquez", "Colombiana")

    # 2. Mostrar sus datos utilizando las propiedades
    print("Datos originales:")
    print("Nombre:", autor.nombre)
    print("Nacionalidad:", autor.nacionalidad)

    # 3. Modificar los datos utilizando los setters
    autor.nombre = "Gabriel García Márquez"
    autor.nacionalidad = "Colombia"

    print()
    print("Datos modificados:")
    print("Nombre:", autor.nombre)
    print("Nacionalidad:", autor.nacionalidad)

    # 4. Intentar asignar un valor vacío
    print()
    print("Prueba de validación:")

    try:
        autor.nombre = ""
    except ValueError as error:
        print("Error:", error)

    try:
        autor.nacionalidad = "   "
    except ValueError as error:
        print("Error:", error)

    # Comprobar que los datos válidos se conservaron
    print()
    print("Datos después de los intentos inválidos:")
    print("Nombre:", autor.nombre)
    print("Nacionalidad:", autor.nacionalidad)


if __name__ == "__main__":
    main()