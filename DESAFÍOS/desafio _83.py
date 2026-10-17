# Desafío 83: Optimizar la búsqueda en una lista ordenada de estudiantes

# Función que realiza la búsqueda binaria
def busqueda_binaria(estudiantes, nombre_buscado):

    # Establecer los límites iniciales de búsqueda
    izquierda = 0
    derecha = len(estudiantes) - 1

    # Repetir mientras existan elementos para buscar
    while izquierda <= derecha:

        # Calcular la posición central
        medio = (izquierda + derecha) // 2

        # Verificar si el estudiante está en el centro
        if estudiantes[medio] == nombre_buscado:
            return medio

        # Si el nombre buscado es menor, buscar a la izquierda
        elif nombre_buscado < estudiantes[medio]:
            derecha = medio - 1

        # Si el nombre buscado es mayor, buscar a la derecha
        else:
            izquierda = medio + 1

    # Devolver -1 si el estudiante no existe
    return -1


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 83: BÚSQUEDA BINARIA DE ESTUDIANTES")
    print()

    # Lista de estudiantes ordenada alfabéticamente
    estudiantes = [
        "Ana",
        "Bruno",
        "Camila",
        "Diego",
        "Emma",
        "Felipe",
        "Gabriel",
        "Lucia",
        "Mateo",
        "Sofia"
    ]

    # Mostrar la lista de estudiantes
    print("LISTA DE ESTUDIANTES:")

    for estudiante in estudiantes:
        print("-", estudiante)

    print()

    # Solicitar el nombre que se desea buscar
    nombre_buscado = input(
        "Ingrese el nombre del estudiante: "
    ).strip().capitalize()

    # Ejecutar la búsqueda binaria
    posicion = busqueda_binaria(estudiantes, nombre_buscado)

    # Mostrar el resultado de la búsqueda
    if posicion != -1:
        print()
        print(f"El estudiante {estudiantes[posicion]} fue encontrado.")
        print(f"Posición en la lista: {posicion + 1}")

    else:
        print()
        print(f"El estudiante {nombre_buscado} no se encuentra en la lista.")