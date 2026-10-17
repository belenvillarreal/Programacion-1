# Desafío 38: Uso del módulo os en un procesador de texto

# Este programa utiliza el módulo os para interactuar con el sistema operativo.
# Permite guardar un texto en un archivo y leer el contenido
# de un archivo existente.

import os


# Crear una función para guardar texto en un archivo
def guardar_archivo(nombre_archivo, contenido):
    """Guarda un texto dentro de un archivo."""

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Archivo guardado correctamente.")


# Crear una función para leer un archivo existente
def leer_archivo(nombre_archivo):
    """Lee y devuelve el contenido de un archivo existente."""

    # Verificar si el archivo existe antes de abrirlo
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        return contenido

    return None


# Crear la función principal del programa
def main():
    print("Desafío 38: Guardar y leer archivos")
    print()

    # Solicitar un texto al usuario
    texto = input("Ingrese un texto para guardar: ")

    # Definir el nombre del archivo
    nombre_archivo = "texto_guardado.txt"

    # Guardar el texto en el archivo
    guardar_archivo(nombre_archivo, texto)

    print()

    # Mostrar la ubicación donde se guardó el archivo
    ruta_actual = os.getcwd()
    print("El archivo fue guardado en:")
    print(ruta_actual)

    print()

    # Leer nuevamente el archivo
    contenido = leer_archivo(nombre_archivo)

    # Mostrar el contenido leído
    if contenido is not None:
        print("Contenido del archivo:")
        print(contenido)
    else:
        print("El archivo no existe.")


# Ejecutar el programa
if __name__ == "__main__":
    main()