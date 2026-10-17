
# Desafío 87: Buscar un libro por autor en un archivo de texto

from pathlib import Path


# Función para buscar todos los libros de un autor
def buscar_libros_por_autor(ruta_archivo, autor_buscado):

    libros_encontrados = []

    try:
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            # Leer cada línea del archivo
            for linea in archivo:

                # Separar el título del libro y su autor
                datos = linea.strip().split(";")

                if len(datos) == 2:
                    titulo = datos[0].strip()
                    autor = datos[1].strip()

                    # Comparar autores sin distinguir mayúsculas
                    if autor.lower() == autor_buscado.lower():
                        libros_encontrados.append(titulo)

        return libros_encontrados

    except FileNotFoundError:
        print("Error: No se encontró el archivo libros.txt.")
        return []

    except OSError as error:
        print(f"Error al leer el archivo: {error}")
        return []


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 87: BÚSQUEDA DE LIBROS POR AUTOR")
    print()

    # Ubicar libros.txt en la carpeta del programa
    ruta_archivo = Path(__file__).resolve().parent / "libros.txt"

    # Crear un archivo de ejemplo solamente si no existe
    if not ruta_archivo.exists():

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Cien años de soledad;Gabriel García Márquez\n")
            archivo.write("El amor en los tiempos del cólera;Gabriel García Márquez\n")
            archivo.write("El principito;Antoine de Saint-Exupéry\n")
            archivo.write("Matilda;Roald Dahl\n")
            archivo.write("Charlie y la fábrica de chocolate;Roald Dahl\n")
            archivo.write("Rayuela;Julio Cortázar\n")

    # Solicitar el autor que se desea buscar
    autor_buscado = input(
        "Ingrese el nombre del autor que desea buscar: "
    ).strip()

    # Ejecutar la búsqueda
    resultados = buscar_libros_por_autor(ruta_archivo, autor_buscado)

    # Mostrar los libros encontrados
    if resultados:
        print(f"\nLibros encontrados de {autor_buscado}:")

        for libro in resultados:
            print("-", libro)

    else:
        print(f"\nNo hay libros de {autor_buscado} en la lista.")
