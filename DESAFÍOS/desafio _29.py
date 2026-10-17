# Desafío 29: Elementos en común entre dos listas
# Este programa crea una función que recibe dos listas
# y devuelve True si tienen al menos un elemento en común.
# En caso contrario, devuelve False.

print("Desafío 29: Elementos en común entre dos listas")


# Crear una función para verificar si dos listas
# tienen al menos un elemento en común
def tienen_elemento_en_comun(lista1, lista2):

    # Recorrer todos los elementos de la primera lista
    for elemento in lista1:

        # Verificar si el elemento también está en la segunda lista
        if elemento in lista2:

            # Si existe un elemento en común, devolver True
            return True

    # Si no se encontró ningún elemento en común,
    # devolver False
    return False


# Crear la función principal del programa
def main():

    # Crear dos listas de ejemplo
    lista_a = [2, 5, 8, 10]
    lista_b = [1, 4, 8, 9]

    # Mostrar las listas
    print("Primera lista:")
    print(lista_a)

    print()

    print("Segunda lista:")
    print(lista_b)

    print()

    # Llamar a la función
    resultado = tienen_elemento_en_comun(lista_a, lista_b)

    # Mostrar el resultado
    print("¿Las listas tienen algún elemento en común?")
    print(resultado)


# Ejecutar el programa
if __name__ == "__main__":
    main()