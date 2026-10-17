# Desafío 32: Verificación y cálculo de números primos
# Este programa permite verificar si un número es primo,
# contar cuántos números primos hay dentro de una lista
# y mostrar los resultados usando funciones reutilizables.

print("Desafío 32: Verificación y cálculo de números primos")

# Crear una función para verificar si un número es primo
def es_primo(numero):

    # Los números menores que 2 no son primos
    if numero < 2:
        return False

    # Revisar posibles divisores solo hasta la raíz cuadrada del número
    # Esto hace que el algoritmo sea más eficiente para números grandes
    for divisor in range(2, int(numero ** 0.5) + 1):

        # Si el número se divide exactamente por otro divisor, no es primo
        if numero % divisor == 0:
            return False

    # Si no se encontró ningún divisor, el número es primo
    return True


# Crear una función para contar cuántos números primos hay en una lista
def contar_primos(lista_numeros):

    # Crear un contador para guardar la cantidad de primos encontrados
    cantidad_primos = 0

    # Recorrer cada número de la lista
    for numero in lista_numeros:

        # Reutilizar la función es_primo para verificar cada número
        if es_primo(numero):

            # Aumentar el contador si el número es primo
            cantidad_primos = cantidad_primos + 1

    # Devolver la cantidad total de números primos encontrados
    return cantidad_primos


# Crear la función principal del programa
def main():

    # Crear una lista de números para analizar
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 20]

    # Mostrar la lista original
    print("Lista de números:")
    print(numeros)

    print()

    # Mostrar si cada número es primo o no
    print("Verificación de números primos:")

    for numero in numeros:

        if es_primo(numero):
            print(numero, "es primo")

        else:
            print(numero, "no es primo")

    print()

    # Usar la función contar_primos para calcular la cantidad total
    cantidad = contar_primos(numeros)

    # Mostrar el resultado final
    print("Cantidad de números primos encontrados:", cantidad)


# Ejecutar el programa desde la función main
main()