# Desafío 31: Palíndromo
# Este programa crea una función llamada es_palindromo
# que recibe una cadena de texto y devuelve True
# si la palabra es un palíndromo o False en caso contrario.

print("Desafío 31: Palíndromo")


# Crear una función para verificar si una palabra es un palíndromo
def es_palindromo(cadena):

    # Convertir la cadena a minúsculas para evitar diferencias
    cadena = cadena.lower()

    # Comparar la cadena original con su versión invertida
    if cadena == cadena[::-1]:

        # Si son iguales, devolver True
        return True

    # Si son diferentes, devolver False
    return False


# Crear la función principal del programa
def main():

    # Solicitar una palabra al usuario
    palabra = input("Ingrese una palabra: ")

    print()

    # Llamar a la función
    resultado = es_palindromo(palabra)

    # Mostrar el resultado
    if resultado:
        print("La palabra es un palíndromo.")

    else:
        print("La palabra no es un palíndromo.")


# Ejecutar el programa
if __name__ == "__main__":
    main()