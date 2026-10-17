
# Desafío 90: Contar las palabras más comunes en un archivo de texto

from pathlib import Path
from collections import Counter
import re


# Función para contar las palabras de un archivo
def contar_palabras(ruta_archivo):

    # Crear un contador para almacenar las frecuencias
    contador = Counter()

    try:
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            # Leer el archivo línea por línea
            for linea in archivo:

                # Convertir el texto a minúsculas
                linea = linea.lower()

                # Extraer palabras sin signos de puntuación
                palabras = re.findall(r"\b[^\W\d_]+\b", linea)

                # Actualizar la cantidad de apariciones
                contador.update(palabras)

        return contador

    except FileNotFoundError:
        print("Error: No se encontró el archivo libros.txt.")
        return Counter()

    except OSError as error:
        print(f"Error al leer el archivo: {error}")
        return Counter()


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 90: PALABRAS MÁS COMUNES")
    print()

    # Buscar libros.txt en la misma carpeta del programa
    ruta_archivo = Path(__file__).resolve().parent / "libros.txt"

    # Contar todas las palabras del archivo
    frecuencias = contar_palabras(ruta_archivo)

    # Mostrar las cinco palabras más frecuentes
    if frecuencias:

        print("LAS 5 PALABRAS MÁS COMUNES:")
        print()

        for palabra, cantidad in frecuencias.most_common(5):
            print(f"{palabra}: {cantidad} veces")

    else:
        print("No se encontraron palabras para contar.")
