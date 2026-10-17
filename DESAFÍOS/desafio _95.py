
# Desafío 95: Análisis de datos de ventas con tuplas

# Lista de ventas: (id_producto, cantidad, precio_unitario)
ventas = [
    (101, 3, 150.0),
    (102, 5, 200.0),
    (103, 2, 350.0),
    (101, 4, 150.0),
    (104, 6, 100.0),
    (102, 3, 200.0),
    (103, 1, 350.0)
]


# Función para calcular el ingreso total
def calcular_ingreso_total(lista_ventas):

    ingreso_total = 0

    for id_producto, cantidad, precio_unitario in lista_ventas:
        ingreso_total += cantidad * precio_unitario

    return ingreso_total


# Función para encontrar el producto más vendido
def encontrar_producto_mas_vendido(lista_ventas):

    # Diccionario para acumular cantidades por producto
    cantidades = {}

    for id_producto, cantidad, precio_unitario in lista_ventas:

        if id_producto in cantidades:
            cantidades[id_producto] += cantidad
        else:
            cantidades[id_producto] = cantidad

    # Identificar el producto con mayor cantidad vendida
    if not cantidades:
        return None, 0

    producto_mas_vendido = max(cantidades, key=cantidades.get)

    return producto_mas_vendido, cantidades[producto_mas_vendido]


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 95: ANÁLISIS DE VENTAS")
    print()

    # Mostrar las ventas registradas
    print("VENTAS REGISTRADAS:")
    print()

    for id_producto, cantidad, precio_unitario in ventas:
        subtotal = cantidad * precio_unitario

        print(f"Producto: {id_producto}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio unitario: ${precio_unitario:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print()

    # Calcular los ingresos totales
    ingreso_total = calcular_ingreso_total(ventas)

    # Encontrar el producto más vendido
    producto, cantidad_vendida = encontrar_producto_mas_vendido(ventas)

    # Mostrar los resultados finales
    print("RESULTADOS FINALES:")
    print()
    print(f"Ingreso total generado: ${ingreso_total:.2f}")

    if producto is not None:
        print(f"Producto más vendido: {producto}")
        print(f"Cantidad total vendida: {cantidad_vendida}")
    else:
        print("No hay ventas registradas.")
