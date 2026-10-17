
# Desafío 50: Ampliación de la clase Autor

# Para hacer más completa la clase Autor, podemos agregar
# atributos como fecha de nacimiento, nacionalidad y género literario.
# También podemos incorporar métodos para mostrar su información,
# agregar libros y consultar sus obras publicadas.


class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, genero):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.libros = []

    def agregar_libro(self, titulo):
        self.libros.append(titulo)

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Fecha de nacimiento:", self.fecha_nacimiento)
        print("Género literario:", self.genero)

    def mostrar_libros(self):
        print("Libros publicados:")
        for libro in self.libros:
            print("-", libro)


# Crear un autor
autor1 = Autor(
    "Mario Benedetti",
    "Uruguaya",
    "14/09/1920",
    "Poesía y narrativa"
)

# Agregar libros
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")

# Mostrar información
autor1.mostrar_informacion()
autor1.mostrar_libros()


# Reflexión:
# Agregar atributos permite guardar más información sobre cada autor.
# Los métodos permiten realizar acciones con esa información,
# como registrar libros y mostrar sus datos.
# Esto hace que la clase Autor sea más completa y útil.
