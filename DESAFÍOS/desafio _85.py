
# Desafío 85: Árbol de clasificación de estudiantes por rendimiento

# Clase que representa cada nodo del árbol
class Nodo:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izquierda = None
        self.derecha = None


# Función para insertar estudiantes en el árbol binario
def insertar(nodo, nombre, promedio):

    # Si no existe un nodo, crear uno nuevo
    if nodo is None:
        return Nodo(nombre, promedio)

    # Los promedios menores se ubican a la izquierda
    if promedio < nodo.promedio:
        nodo.izquierda = insertar(nodo.izquierda, nombre, promedio)

    # Los promedios mayores o iguales se ubican a la derecha
    else:
        nodo.derecha = insertar(nodo.derecha, nombre, promedio)

    return nodo


# Función recursiva para recorrer el árbol en inorden
def recorrer_inorden(nodo):

    if nodo is not None:

        # Primero recorrer el subárbol izquierdo
        recorrer_inorden(nodo.izquierda)

        # Mostrar el estudiante y su promedio
        print(f"Estudiante: {nodo.nombre} - Promedio: {nodo.promedio}")

        # Finalmente recorrer el subárbol derecho
        recorrer_inorden(nodo.derecha)


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 85: ÁRBOL DE RENDIMIENTO ACADÉMICO")
    print()

    # Lista de estudiantes y sus promedios
    estudiantes = [
        ("Ana", 8.5),
        ("Lucas", 6.8),
        ("Sofia", 9.7),
        ("Mateo", 7.4),
        ("Camila", 9.2),
        ("Bruno", 5.9)
    ]

    # Crear el árbol inicialmente vacío
    raiz = None

    # Insertar todos los estudiantes en el árbol
    for nombre, promedio in estudiantes:
        raiz = insertar(raiz, nombre, promedio)

    # Mostrar los estudiantes en orden ascendente
    print("ESTUDIANTES ORDENADOS POR RENDIMIENTO:")
    print()

    recorrer_inorden(raiz)
