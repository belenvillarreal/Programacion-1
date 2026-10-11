
# Desafío 92: Selección de múltiples elementos únicos

import random


# Función para seleccionar ganadores sin repetir participantes
def seleccionar_ganadores(participantes, cantidad_ganadores):

    # Seleccionar elementos únicos de forma aleatoria
    ganadores = random.sample(participantes, cantidad_ganadores)

    return ganadores


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 92: SORTEO DE GANADORES")
    print()

    # Lista de participantes del sorteo
    participantes = [
        "Ana", "Bruno", "Camila", "Diego", "Emma",
        "Felipe", "Gabriel", "Lucia", "Mateo", "Sofia",
        "Valentina", "Joaquin", "Martina", "Lucas", "Florencia"
    ]

    # Mostrar los participantes
    print("PARTICIPANTES DEL SORTEO:")

    for participante in participantes:
        print("-", participante)

    print()

    # Solicitar la cantidad de ganadores
    try:
        cantidad_ganadores = int(
            input("Ingrese la cantidad de ganadores: ")
        )

        # Verificar que la cantidad sea válida
        if 1 <= cantidad_ganadores <= len(participantes):

            # Realizar el sorteo
            ganadores = seleccionar_ganadores(
                participantes, cantidad_ganadores
            )

            # Mostrar los ganadores seleccionados
            print("\nGANADORES DEL SORTEO:")

            for i, ganador in enumerate(ganadores, start=1):
                print(f"Ganador {i}: {ganador}")

            print("\nTodos los ganadores son únicos.")

        else:
            print(
                "Error: La cantidad debe estar entre 1 y",
                len(participantes)
            )

    except ValueError:
        print("Error: Debe ingresar un número entero.")
