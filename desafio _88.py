
# Desafío 88: Actualizar la cantidad de libros disponibles en un archivo CSV

import csv
from pathlib import Path


# Función para actualizar las copias de un libro
def actualizar_inventario(ruta_archivo, libro_buscado, nueva_cantidad):

    inventario = []
    encontrado = False

    # Leer el archivo CSV
    with open(ruta_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:

            # Buscar el libro sin distinguir mayúsculas
            if fila["libro"].strip().lower() == libro_buscado.lower():

                # Actualizar la cantidad de copias
                fila["copias"] = str(nueva_cantidad)
                encontrado = True

            inventario.append(fila)

    # Guardar los cambios solamente si se encontró el libro
    if encontrado:

        with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:

            campos = ["libro", "copias"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            # Escribir los encabezados y los datos actualizados
            escritor.writeheader()
            escritor.writerows(inventario)

    return encontrado


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 88: ACTUALIZACIÓN DE INVENTARIO")
    print()

    # Ubicar el archivo CSV en la carpeta del programa
    ruta_archivo = Path(__file__).resolve().parent / "inventario.csv"

    # Crear un inventario de ejemplo si todavía no existe
    if not ruta_archivo.exists():

        with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)
            escritor.writerow(["libro", "copias"])
            escritor.writerow(["El principito", 5])
            escritor.writerow(["Matilda", 8])
            escritor.writerow(["Cien años de soledad", 3])
            escritor.writerow(["Rayuela", 6])

    # Mostrar el inventario actual
    print("INVENTARIO ACTUAL:")

    with open(ruta_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            print(f"{fila['libro']}: {fila['copias']} copias")

    print()

    # Solicitar los datos al usuario
    libro_buscado = input("Ingrese el nombre del libro: ").strip()

    try:
        nueva_cantidad = int(input("Ingrese la nueva cantidad de copias: "))

        # No permitir cantidades negativas
        if nueva_cantidad < 0:
            print("Error: La cantidad de copias no puede ser negativa.")

        else:
            # Actualizar el archivo CSV
            encontrado = actualizar_inventario(
                ruta_archivo, libro_buscado, nueva_cantidad
            )

            if encontrado:
                print("\nInventario actualizado correctamente.")
                print(f"{libro_buscado}: {nueva_cantidad} copias disponibles.")

            else:
                print("\nEl libro no se encuentra en el inventario.")

    except ValueError:
        print("Error: Debe ingresar un número entero.")
