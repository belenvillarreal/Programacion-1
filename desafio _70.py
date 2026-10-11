
# Desafío 70: Excepción personalizada para raíces cuadradas

import math


# Crear una excepción personalizada
class NegativeNumberError(Exception):
    """Excepción que se produce al ingresar un número negativo."""
    pass


# Función para calcular la raíz cuadrada
def calcular_raiz_cuadrada(numero):
    # Validar que el número no sea negativo
    if numero < 0:
        raise NegativeNumberError(
            "No se puede calcular la raíz cuadrada de un número negativo."
        )

    # Calcular y devolver la raíz cuadrada
    return math.sqrt(numero)


# Programa principal
def main():
    print("DESAFÍO 70: CÁLCULO DE RAÍCES CUADRADAS")
    print()

    try:
        # Solicitar un número al usuario
        numero = float(input("Ingrese un número: "))

        # Calcular la raíz cuadrada
        resultado = calcular_raiz_cuadrada(numero)

    except NegativeNumberError as error:
        # Capturar la excepción personalizada
        print("Error:", error)
        print("Por favor, ingrese un número mayor o igual a cero.")

    except ValueError:
        # Capturar entradas no numéricas
        print("Error: Debe ingresar un número válido.")

    else:
        # Mostrar el resultado si no hubo errores
        print(f"La raíz cuadrada de {numero} es: {resultado}")

    finally:
        print("Fin del programa.")


if __name__ == "__main__":
    main()


# Reflexión:
# NegativeNumberError es una excepción personalizada
# que hereda de la clase Exception.
# La instrucción raise permite lanzar esta excepción
# cuando el usuario ingresa un número negativo.
# El bloque try-except captura el error y muestra
# un mensaje claro sin interrumpir bruscamente el programa.
