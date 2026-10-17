# Desafío 44: TAD Biblioteca

# Este programa implementa un Tipo Abstracto de Datos (TAD)
# sencillo para gestionar los libros de una biblioteca.
# Utiliza una lista para almacenar los libros y funciones
# independientes para agregar, eliminar, buscar y mostrar libros.


# Función para agregar un libro a la biblioteca
def agregar_libro(biblioteca, titulo):
    # Verificar que el libro no esté previamente en la colección
    if titulo not in biblioteca:
        biblioteca.append(titulo)
        print("Libro agregado:", titulo)
    else:
        print("El libro ya se encuentra en la biblioteca:", titulo)


# Función para eliminar un libro de la biblioteca
def eliminar_libro(biblioteca, titulo):
    # Verificar que el libro exista antes de eliminarlo
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("Libro eliminado:", titulo)
    else:
        print("No se encontró el libro:", titulo)


# Función para buscar un libro por su título
def buscar_libro(biblioteca, titulo):
    # Recorrer la colección para buscar el título solicitado
    for libro in biblioteca:
        if libro.lower() == titulo.lower():
            return libro

    # Si no se encuentra el libro, devolver None
    return None


# Función para mostrar todos los libros disponibles
def mostrar_libros(biblioteca):
    print()
    print("Libros disponibles en la biblioteca:")

    # Verificar si existen libros para mostrar
    if len(biblioteca) == 0:
        print("La biblioteca no tiene libros disponibles.")
    else:
        # Recorrer y mostrar todos los libros de la colección
        for libro in biblioteca:
            print("-", libro)


# Función principal del programa
def main():
    print("Desafío 44: TAD Biblioteca")
    print()

    # Crear la colección donde se almacenarán los libros
    biblioteca = []

    # Agregar al menos cuatro libros para probar el TAD
    agregar_libro(biblioteca, "El Principito")
    agregar_libro(biblioteca, "Don Quijote de la Mancha")
    agregar_libro(biblioteca, "Cien años de soledad")
    agregar_libro(biblioteca, "Alicia en el país de las maravillas")

    # Mostrar todos los libros agregados
    mostrar_libros(biblioteca)

    # Realizar una búsqueda por título
    print()
    print("Búsqueda de un libro:")

    titulo_buscado = "El Principito"
    resultado = buscar_libro(biblioteca, titulo_buscado)

    if resultado is not None:
        print("Libro encontrado:", resultado)
    else:
        print("No se encontró el libro:", titulo_buscado)

    # Eliminar uno de los libros
    print()
    print("Eliminación de un libro:")
    eliminar_libro(biblioteca, "Don Quijote de la Mancha")

    # Mostrar nuevamente la colección para comprobar la eliminación
    mostrar_libros(biblioteca)


# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()