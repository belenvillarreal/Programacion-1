
# Desafío 81: Recorrido de estudiantes por niveles

from collections import deque


# Clase que representa un grado y sus estudiantes
class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.hijos = []


    # Agregar un grado hijo al árbol
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


# Función para recorrer el árbol por niveles
def recorrer_por_niveles(raiz):

    if raiz is None:
        print("El árbol está vacío.")
        return

    # Crear una cola para recorrer el árbol
    cola = deque([raiz])

    # Recorrer los nodos desde la raíz
    while cola:
        nodo_actual = cola.popleft()

        # Mostrar el grado y sus estudiantes
        print(f"Grado {nodo_actual.grado}:")
        for estudiante in nodo_actual.estudiantes:
            print(f"  - {estudiante}")

        print()

        # Agregar los hijos a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 81: RECORRIDO DE ESTUDIANTES")
    print()

    # Crear los nodos con grados y estudiantes
    grados = {}

    for grado in range(12, 0, -1):
        grados[grado] = Nodo(
            grado,
            [f"Estudiante A{grado}", f"Estudiante B{grado}"]
        )

    # Construir el árbol con grados descendentes
    for grado in range(12, 1, -1):
        grados[grado].agregar_hijo(grados[grado - 1])

    # La raíz corresponde al grado más alto
    raiz = grados[12]

    # Mostrar todos los grados y estudiantes
    recorrer_por_niveles(raiz)
