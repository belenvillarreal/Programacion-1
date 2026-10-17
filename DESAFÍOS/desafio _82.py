
# Desafío 82: Búsqueda secuencial en una tabla de calificaciones

def buscar_calificacion(matriz, estudiantes, materias, calificacion):
    """
    Busca una calificación recorriendo toda la matriz.
    Devuelve los estudiantes y materias donde aparece.
    """
    resultados = []

    # Recorrer las filas (estudiantes)
    for i in range(len(matriz)):

        # Recorrer las columnas (materias)
        for j in range(len(matriz[i])):

            # Comparar cada calificación con la buscada
            if matriz[i][j] == calificacion:
                resultados.append((estudiantes[i], materias[j]))

    return resultados


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 82: BÚSQUEDA DE CALIFICACIONES")
    print()

    # Nombres de los estudiantes
    estudiantes = ["Ana", "Lucas", "Sofía", "Mateo"]

    # Materias correspondientes a las columnas
    materias = ["Matemática", "Lengua", "Ciencias"]

    # Cada fila contiene las calificaciones de un estudiante
    calificaciones = [
        [8, 9, 7],    # Ana
        [6, 8, 10],   # Lucas
        [9, 7, 8],    # Sofía
        [10, 9, 6]    # Mateo
    ]

    # Mostrar la tabla
    print("TABLA DE CALIFICACIONES")
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]}: {calificaciones[i]}")

    print()

    # Solicitar la calificación que se desea buscar
    try:
        nota_buscada = int(input("Ingrese la calificación a buscar: "))

        # Realizar la búsqueda secuencial
        resultados = buscar_calificacion(
            calificaciones, estudiantes, materias, nota_buscada
        )

        # Mostrar los resultados encontrados
        if resultados:
            print(f"\nLa calificación {nota_buscada} se encontró en:")

            for estudiante, materia in resultados:
                print(f"Estudiante: {estudiante} - Materia: {materia}")

        else:
            print(f"La calificación {nota_buscada} no se encontró.")

    except ValueError:
        print("Error: Debe ingresar una calificación numérica entera.")
