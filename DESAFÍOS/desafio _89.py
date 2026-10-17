
# Desafío 89: Eliminar registros de un archivo de préstamos

from pathlib import Path


# Función para leer los préstamos guardados
def leer_prestamos(ruta_archivo):

    # Comprobar si existe el archivo
    if not ruta_archivo.exists():
        print("No se encontró el archivo prestamos.txt.")
        return []

    # Leer todo el contenido del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    # Separar los préstamos utilizando la línea divisoria
    registros = contenido.split("------------------------------")

    # Eliminar los espacios y registros vacíos
    prestamos = []

    for registro in registros:
        registro = registro.strip()

        if registro:
            prestamos.append(registro)

    return prestamos


# Función para mostrar los préstamos disponibles
def mostrar_prestamos(prestamos):

    print("REGISTROS DE PRÉSTAMOS:")
    print()

    # Mostrar cada registro con su número
    for i, prestamo in enumerate(prestamos, start=1):
        print(f"Préstamo {i}:")
        print(prestamo)
        print("------------------------------")


# Función para eliminar un préstamo seleccionado
def eliminar_prestamo(ruta_archivo, prestamos, numero):

    # Eliminar el registro de la lista
    prestamos.pop(numero - 1)

    # Actualizar el archivo con los registros restantes
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:

        for prestamo in prestamos:
            archivo.write(prestamo + "\n")
            archivo.write("------------------------------\n")

    print("\n¡Préstamo eliminado correctamente!")


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 89: ELIMINAR PRÉSTAMOS DE LIBROS")
    print()

    # Utilizar el mismo archivo del Desafío 86
    ruta_archivo = Path(__file__).resolve().parent / "prestamos.txt"

    try:
        # Leer los préstamos existentes
        prestamos = leer_prestamos(ruta_archivo)

        # Comprobar si hay préstamos registrados
        if not prestamos:
            print("No hay préstamos registrados para eliminar.")

        else:
            # Mostrar los registros actuales
            mostrar_prestamos(prestamos)

            # Solicitar el número del préstamo a eliminar
            numero = int(input(
                "\nIngrese el número del préstamo que desea eliminar: "
            ))

            # Verificar que el número sea válido
            if 1 <= numero <= len(prestamos):

                # Eliminar el registro seleccionado
                eliminar_prestamo(ruta_archivo, prestamos, numero)

                # Mostrar los registros restantes
                print("\nPRÉSTAMOS ACTUALIZADOS:")
                print()

                if prestamos:
                    mostrar_prestamos(prestamos)
                else:
                    print("No quedan préstamos registrados.")

            else:
                print("Error: El número de préstamo no existe.")

    except ValueError:
        print("Error: Debe ingresar un número entero.")

    except OSError as error:
        print(f"Error al trabajar con el archivo: {error}")
