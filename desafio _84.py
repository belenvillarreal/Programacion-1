
# Desafío 84: Ordenar estudiantes por promedio de calificaciones

# Función para ordenar mediante el algoritmo de selección
def ordenar_por_seleccion(estudiantes):

    cantidad = len(estudiantes)

    # Recorrer las posiciones de la lista
    for i in range(cantidad - 1):

        # Suponer que el mayor promedio está en la posición actual
        indice_mayor = i

        # Buscar el promedio más alto entre los restantes
        for j in range(i + 1, cantidad):

            if estudiantes[j][1] > estudiantes[indice_mayor][1]:
                indice_mayor = j

        # Intercambiar posiciones si se encontró un promedio mayor
        if indice_mayor != i:
            estudiantes[i], estudiantes[indice_mayor] = (
                estudiantes[indice_mayor],
                estudiantes[i]
            )

    return estudiantes


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 84: ORDENAMIENTO POR SELECCIÓN")
    print()

    # Lista de estudiantes y sus promedios
    estudiantes = [
        ["Ana", 8.5],
        ["Lucas", 6.8],
        ["Sofia", 9.7],
        ["Mateo", 7.4],
        ["Camila", 9.2]
    ]

    # Mostrar la lista original
    print("ESTUDIANTES ANTES DE ORDENAR:")

    for nombre, promedio in estudiantes:
        print(f"{nombre}: {promedio}")

    print()

    # Ordenar de mayor a menor mediante selección
    ordenar_por_seleccion(estudiantes)

    # Mostrar la lista ordenada
    print("ESTUDIANTES ORDENADOS POR PROMEDIO:")

    for nombre, promedio in estudiantes:
        print(f"{nombre}: {promedio}")

    print()

    # Mostrar al estudiante con el promedio más alto
    print("ESTUDIANTE CON EL PROMEDIO MÁS ALTO:")
    print(f"{estudiantes[0][0]} - Promedio: {estudiantes[0][1]}")
