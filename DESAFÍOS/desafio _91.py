
# Desafío 91: Generación de números de punto flotante
# Simulación de temperaturas climáticas aleatorias

import random


# Función para generar temperaturas aleatorias
def generar_temperaturas(cantidad):

    # Lista para almacenar las temperaturas generadas
    temperaturas = []

    # Generar la cantidad de temperaturas solicitada
    for i in range(cantidad):

        # Crear una temperatura aleatoria entre -10.0 y 40.0
        temperatura = random.uniform(-10.0, 40.0)

        # Guardar la temperatura en la lista
        temperaturas.append(temperatura)

    # Devolver la lista completa
    return temperaturas


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 91: SIMULACIÓN DE TEMPERATURAS")
    print()

    # Cantidad de temperaturas para la simulación
    cantidad_temperaturas = 20

    # Generar y almacenar las temperaturas
    temperaturas = generar_temperaturas(cantidad_temperaturas)

    # Mostrar las temperaturas generadas
    print("TEMPERATURAS GENERADAS:")
    print()

    for i, temperatura in enumerate(temperaturas, start=1):
        print(f"Temperatura {i}: {temperatura:.2f} °C")

    print()
    print(f"Total de temperaturas generadas: {len(temperaturas)}")
    print("Las temperaturas quedaron almacenadas en una lista.")
