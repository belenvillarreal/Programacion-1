# Desafío 45: Dos bibliotecas, un mismo TAD

# Este programa gestiona dos bibliotecas diferentes utilizando
# las mismas funciones para agregar, eliminar, buscar y mostrar libros.
# Cada biblioteca mantiene su propia lista de libros de forma independiente.


# Agregar un libro a la biblioteca indicada
def agregar(biblioteca, titulo):
    if titulo not in biblioteca:
        biblioteca.append(titulo)
        print("Libro agregado:", titulo)
    else:
        print("El libro ya existe:", titulo)


# Eliminar un libro de la biblioteca indicada
def eliminar(biblioteca, titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("Libro eliminado:", titulo)
    else:
        print("No se encontró el libro:", titulo)


# Buscar un libro por título
def buscar(biblioteca, titulo):
    for libro in biblioteca:
        if libro.lower() == titulo.lower():
            return libro

    return None


# Mostrar el contenido de una biblioteca
def mostrar(nombre_biblioteca, biblioteca):
    print()
    print(nombre_biblioteca)

    if len(biblioteca) == 0:
        print("No hay libros disponibles.")
    else:
        for libro in biblioteca:
            print("-", libro)


# Función principal
def main():
    print("Desafío 45: Dos bibliotecas, un mismo TAD")

    # Crear dos colecciones independientes
    biblioteca_1 = []
    biblioteca_2 = []

    # Agregar libros a la primera biblioteca
    agregar(biblioteca_1, "El Principito")
    agregar(biblioteca_1, "Don Quijote de la Mancha")
    agregar(biblioteca_1, "Cien años de soledad")

    # Agregar libros a la segunda biblioteca
    agregar(biblioteca_2, "Rayuela")
    agregar(biblioteca_2, "1984")
    agregar(biblioteca_2, "La Odisea")

    # Realizar búsquedas en ambas bibliotecas
    print()
    print("Búsqueda en Biblioteca 1:")
    resultado_1 = buscar(biblioteca_1, "El Principito")

    if resultado_1 is not None:
        print("Libro encontrado:", resultado_1)
    else:
        print("Libro no encontrado.")

    print()
    print("Búsqueda en Biblioteca 2:")
    resultado_2 = buscar(biblioteca_2, "1984")

    if resultado_2 is not None:
        print("Libro encontrado:", resultado_2)
    else:
        print("Libro no encontrado.")

    # Eliminar un libro de cada biblioteca
    print()
    print("Eliminaciones:")
    eliminar(biblioteca_1, "Don Quijote de la Mancha")
    eliminar(biblioteca_2, "La Odisea")

    # Mostrar el contenido final de ambas bibliotecas
    mostrar("Biblioteca 1:", biblioteca_1)
    mostrar("Biblioteca 2:", biblioteca_2)

    # Reflexión final solicitada
    print()
    print("Reflexión:")
    print(
        "Pasar constantemente la colección a cada función puede volver "
        "el código más difícil de mantener."
    )
    print(
        "Una posible mejora sería reunir los datos y las operaciones "
        "de cada biblioteca en una misma estructura."
    )


# Ejecutar el programa
if __name__ == "__main__":
    main()