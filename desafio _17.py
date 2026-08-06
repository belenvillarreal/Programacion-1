# Desafío 3: Simulación de una Carrera de Autos
# Este programa simula una carrera de cuatro autos durante 10 segundos.
# Cada auto recibe una velocidad aleatoria y avanza en cada segundo
# una distancia igual a su velocidad. Al finalizar, se muestra
# el auto ganador o todos los autos ganadores si ocurre un empate.

print("Desafío 3: Simulación de una Carrera de Autos")

# Importar la biblioteca random para generar velocidades aleatorias
import random

# Crear una lista con los autos que participarán en la carrera
autos = ["Auto 1", "Auto 2", "Auto 3", "Auto 4"]

# Crear un diccionario para guardar la velocidad de cada auto
velocidades = {}

# Crear otro diccionario para guardar la distancia recorrida por cada auto
distancias = {}

# Asignar una velocidad aleatoria a cada auto
# e iniciar su distancia recorrida en 0 metros
for auto in autos:

    # Generar una velocidad aleatoria entre 10 y 30 metros por segundo
    velocidades[auto] = random.randint(10, 30)

    # Iniciar la distancia recorrida del auto en 0
    distancias[auto] = 0

# Mostrar las velocidades asignadas a los autos
print("Velocidades de los autos:")

for auto in autos:
    print(auto, ":", velocidades[auto], "m/s")

# Dejar una línea en blanco para ordenar la salida
print()

# Simular los 10 segundos de la carrera
for segundo in range(1, 11):

    # Mostrar el segundo actual
    print("Segundo", segundo)

    # Actualizar la distancia recorrida por cada auto
    for auto in autos:

        # Cada auto avanza una distancia igual a su velocidad
        distancias[auto] = distancias[auto] + velocidades[auto]

        # Mostrar la distancia acumulada del auto
        print(auto, "ha recorrido", distancias[auto], "metros")

    # Dejar una línea en blanco entre cada segundo
    print()

# Buscar la mayor distancia recorrida
distancia_maxima = max(distancias.values())

# Crear una lista para guardar al ganador o a los ganadores
ganadores = []

# Recorrer los autos para encontrar cuáles alcanzaron la distancia máxima
for auto in autos:

    # Si la distancia del auto coincide con la máxima, es ganador
    if distancias[auto] == distancia_maxima:
        ganadores.append(auto)

# Mostrar el resultado final de la carrera
print("RESULTADO FINAL:")

# Verificar si hubo un único ganador
if len(ganadores) == 1:
    print("El ganador es:", ganadores[0])

# Si hay más de un ganador, significa que ocurrió un empate
else:
    print("Hubo un empate entre los siguientes autos:")

    # Mostrar todos los autos que empataron
    for auto in ganadores:
        print(auto)

# Mostrar la distancia máxima alcanzada
print("Distancia recorrida:", distancia_maxima, "metros")