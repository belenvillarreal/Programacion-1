
# Desafío extra: Simulación de lanzamiento de dados

import random


# Función para simular el lanzamiento de dos dados
def lanzar_dados():

    # Posibles resultados de un dado
    caras = [1, 2, 3, 4, 5, 6]

    # Seleccionar dos resultados aleatorios con random.choices()
    # Al no indicar pesos, todos los números tienen igual probabilidad
    resultados = random.choices(caras, k=2)

    return resultados


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO EXTRA: LANZAMIENTO DE DADOS")
    print()

    # Simular el lanzamiento de los dos dados
    dados = lanzar_dados()

    # Mostrar los resultados obtenidos
    print("RESULTADOS DEL LANZAMIENTO:")
    print(f"Dado 1: {dados[0]}")
    print(f"Dado 2: {dados[1]}")

    # Calcular y mostrar la suma de ambos dados
    suma = dados[0] + dados[1]

    print()
    print(f"Suma de los dos dados: {suma}")
