# Desafío 57: Herencia - clase Poeta

# La clase Autor contiene los datos básicos de un autor.
# La clase Poeta hereda de Autor y agrega el atributo tipo_poesia.


class Autor:
    """Representa a un autor con nombre y nacionalidad."""

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_autor(self):
        """Muestra los datos básicos del autor."""
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)


class Poeta(Autor):
    """Representa a un poeta que hereda de la clase Autor."""

    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Inicializar los atributos heredados de Autor
        super().__init__(nombre, nacionalidad)

        # Atributo propio de Poeta
        self.tipo_poesia = tipo_poesia

    def mostrar_informacion(self):
        """Muestra toda la información del poeta."""
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Tipo de poesía:", self.tipo_poesia)


def main():
    """Demuestra el funcionamiento de la herencia."""

    print("Desafío 57: Herencia - clase Poeta")
    print()

    # Crear dos objetos de la clase Poeta
    poeta_1 = Poeta(
        "Mario Benedetti",
        "Uruguaya",
        "Poesía lírica"
    )

    poeta_2 = Poeta(
        "Juana de Ibarbourou",
        "Uruguaya",
        "Poesía lírica"
    )

    # Mostrar toda la información de los poetas
    print("Datos del primer poeta:")
    poeta_1.mostrar_informacion()

    print()

    print("Datos del segundo poeta:")
    poeta_2.mostrar_informacion()

    # Verificar el uso de un método heredado de Autor
    print()
    print("Uso de un método heredado de Autor:")
    poeta_1.mostrar_autor()

    # Verificar el acceso a atributos heredados
    print()
    print("Acceso a atributos heredados:")
    print("Nombre heredado:", poeta_2.nombre)
    print("Nacionalidad heredada:", poeta_2.nacionalidad)


if __name__ == "__main__":
    main()