# Desafío 39: Calculadora de Fechas

# Este programa permite ingresar dos fechas y calcular la diferencia
# entre ellas utilizando el módulo datetime de Python.
# El módulo datetime permite trabajar correctamente con fechas,
# incluyendo meses con distinta cantidad de días y años bisiestos.

from datetime import datetime


# Crear una función para solicitar una fecha al usuario
def ingresar_fecha(mensaje):
    # Pedir al usuario que ingrese una fecha en formato día/mes/año
    fecha_texto = input(mensaje)

    # Convertir el texto ingresado en un objeto de tipo fecha
    fecha = datetime.strptime(fecha_texto, "%d/%m/%Y")

    # Devolver la fecha convertida
    return fecha


# Crear una función para calcular la diferencia entre dos fechas
def calcular_diferencia(fecha1, fecha2):
    # Restar las fechas y utilizar abs para obtener
    # una diferencia positiva sin importar el orden ingresado
    diferencia = abs(fecha2 - fecha1)

    # Devolver la cantidad de días entre ambas fechas
    return diferencia.days


# Crear la función principal del programa
def main():
    print("Desafío 39: Calculadora de Fechas")
    print()

    # Solicitar las dos fechas al usuario
    fecha1 = ingresar_fecha("Ingrese la primera fecha (DD/MM/AAAA): ")
    fecha2 = ingresar_fecha("Ingrese la segunda fecha (DD/MM/AAAA): ")

    # Calcular la diferencia entre las fechas
    dias_diferencia = calcular_diferencia(fecha1, fecha2)

    print()

    # Mostrar las fechas ingresadas
    print("Primera fecha:", fecha1.strftime("%d/%m/%Y"))
    print("Segunda fecha:", fecha2.strftime("%d/%m/%Y"))

    # Mostrar el resultado
    print("La diferencia entre las dos fechas es de",
          dias_diferencia, "días.")


# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()