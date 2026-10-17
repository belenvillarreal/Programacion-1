
# Desafío 99: Simulación climática con tuplas

# Lista de registros climáticos
# Cada tupla contiene: (ciudad, temperatura, humedad)
registros_climaticos = [
    ("Mercedes", 28.5, 65),
    ("Montevideo", 24.0, 72),
    ("Salto", 32.5, 58),
    ("Paysandú", 30.0, 60),
    ("Colonia", 22.5, 75),
    ("Rivera", 26.0, 70)
]


# Función para encontrar las temperaturas extremas
def obtener_temperaturas_extremas(registros):

    # Buscar la tupla con mayor temperatura
    ciudad_mas_calurosa = max(
        registros, key=lambda registro: registro[1]
    )

    # Buscar la tupla con menor temperatura
    ciudad_mas_fria = min(
        registros, key=lambda registro: registro[1]
    )

    return ciudad_mas_calurosa, ciudad_mas_fria


# Función para calcular el promedio de humedad
def calcular_promedio_humedad(registros):

    # Sumar la humedad de todos los registros
    suma_humedad = 0

    for ciudad, temperatura, humedad in registros:
        suma_humedad += humedad

    # Calcular el promedio general
    promedio = suma_humedad / len(registros)

    return promedio


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 99: SIMULACIÓN CLIMÁTICA")
    print()

    # Mostrar los registros climáticos
    print("REGISTROS CLIMÁTICOS:")
    print()

    for ciudad, temperatura, humedad in registros_climaticos:
        print(f"Ciudad: {ciudad}")
        print(f"Temperatura: {temperatura:.1f} °C")
        print(f"Humedad: {humedad}%")
        print()

    # Obtener las ciudades con temperaturas extremas
    mas_calurosa, mas_fria = obtener_temperaturas_extremas(
        registros_climaticos
    )

    # Calcular el promedio general de humedad
    promedio_humedad = calcular_promedio_humedad(
        registros_climaticos
    )

    # Mostrar los resultados finales
    print("RESULTADOS FINALES:")
    print()

    print(
        f"Ciudad con temperatura más alta: "
        f"{mas_calurosa[0]} ({mas_calurosa[1]:.1f} °C)"
    )

    print(
        f"Ciudad con temperatura más baja: "
        f"{mas_fria[0]} ({mas_fria[1]:.1f} °C)"
    )

    print(f"Promedio general de humedad: {promedio_humedad:.2f}%")
