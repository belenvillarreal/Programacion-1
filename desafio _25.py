print("Desafío 25: Batalla Naval")

# Importar NumPy para crear y trabajar con matrices
import numpy as np

# Importar random para generar posiciones aleatorias
import random

# Crear un tablero de 5x5 lleno de ceros
# Los ceros representan agua
tablero = np.zeros((5, 5), dtype=int)

# Crear un contador para saber cuántos barcos ya fueron colocados
barcos_colocados = 0

# Colocar exactamente 3 barcos en posiciones aleatorias
while barcos_colocados < 3:

    # Generar una fila aleatoria entre 0 y 4
    x = random.randint(0, 4)

    # Generar una columna aleatoria entre 0 y 4
    y = random.randint(0, 4)

    # Verificar que en esa posición no haya un barco todavía
    if tablero[x, y] == 0:

        # Colocar un barco usando el número 1
        tablero[x, y] = 1

        # Aumentar el contador de barcos colocados
        barcos_colocados = barcos_colocados + 1

# Mostrar el tablero para comprobar dónde quedaron los barcos
print("Tablero de juego:")
print(tablero)

print()

# Crear una función que reciba las coordenadas x e y
def disparar(x, y):

    # Verificar si las coordenadas están dentro del tablero
    if x < 0 or x > 4 or y < 0 or y > 4:
        print("Coordenadas fuera del tablero.")

    else:
        # Verificar si en esa posición hay un barco
        if tablero[x, y] == 1:
            print("¡Golpeaste un barco!")

        # Si no hay barco, entonces hay agua
        else:
            print("El disparo cayó al agua.")

# Probar la función con algunas coordenadas
print("Prueba de disparos:")

disparar(0, 0)
disparar(2, 3)
disparar(4, 4)