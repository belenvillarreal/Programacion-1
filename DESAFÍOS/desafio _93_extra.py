
# Desafío extra: Gestión de coordenadas de satélites

import math


# Función para calcular la distancia de un satélite al origen
def calcular_distancia(coordenadas):

    # Obtener las coordenadas de la tupla
    x, y, z = coordenadas

    # Calcular la distancia al origen (0, 0, 0)
    distancia = math.sqrt(x**2 + y**2 + z**2)

    return distancia


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO EXTRA: COORDENADAS DE SATÉLITES")
    print()

    # Diccionario con cinco satélites y sus coordenadas
    # Las coordenadas se almacenan como tuplas inmutables
    satelites = {
        "Satélite 1": (3, 4, 0),
        "Satélite 2": (10, 20, 30),
        "Satélite 3": (5, 12, 0),
        "Satélite 4": (8, 15, 6),
        "Satélite 5": (1, 2, 2)
    }

    # Diccionario para almacenar las distancias calculadas
    distancias = {}

    print("DISTANCIAS DE LOS SATÉLITES AL ORIGEN:")
    print()

    # Recorrer todos los satélites
    for nombre, coordenadas in satelites.items():

        # Calcular la distancia al origen
        distancia = calcular_distancia(coordenadas)

        # Guardar la distancia correspondiente
        distancias[nombre] = distancia

        # Mostrar las coordenadas y la distancia
        print(f"{nombre}:")
        print(f"Coordenadas: {coordenadas}")
        print(f"Distancia al origen: {distancia:.2f}")
        print()

    # Identificar el satélite más cercano al origen
    mas_cercano = min(distancias, key=distancias.get)

    # Identificar el satélite más lejano al origen
    mas_lejano = max(distancias, key=distancias.get)

    # Mostrar los resultados finales
    print("RESULTADOS FINALES:")
    print()

    print(f"Satélite más cercano: {mas_cercano}")
    print(f"Distancia: {distancias[mas_cercano]:.2f}")

    print()

    print(f"Satélite más lejano: {mas_lejano}")
    print(f"Distancia: {distancias[mas_lejano]:.2f}")
