
# Desafío 67: Manejo de excepciones en Python
# División de dos números enteros

def dividir_numeros():
    try:
        # Solicitar los números al usuario
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))

        # Realizar la división
        resultado = numero1 / numero2

    except ValueError:
        # Error cuando se ingresan letras u otros valores no válidos
        print("Error: Debe ingresar números enteros válidos, no letras ni otros caracteres.")

    except ZeroDivisionError:
        # Error cuando el segundo número es cero
        print("Error: No es posible dividir entre cero. Ingrese un divisor diferente de cero.")

    else:
        # Mostrar el resultado si no ocurrió ningún error
        print(f"El resultado de dividir {numero1} entre {numero2} es: {resultado}")

    finally:
        # Mensaje que se muestra siempre
        print("Fin de la operación.")


# Programa principal
if __name__ == "__main__":
    print("DESAFÍO 67: DIVISIÓN CON MANEJO DE EXCEPCIONES")
    print()
    dividir_numeros()


# Reflexión:
# El bloque try permite intentar realizar la división.
# ValueError controla los valores que no son números enteros.
# ZeroDivisionError evita que el programa falle al dividir por cero.
# El bloque else muestra el resultado cuando no hay errores.
# El bloque finally se ejecuta siempre, ocurra o no una excepción.
