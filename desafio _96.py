
# Desafío 96: Inventario de productos con diccionarios

# Diccionario principal del inventario
# Cada código identifica un producto con nombre, precio y stock
inventario = {
    "P001": {"nombre": "Teclado", "precio": 850.0, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 450.0, "stock": 15},
    "P003": {"nombre": "Monitor", "precio": 6500.0, "stock": 5}
}


# Función para agregar nuevos productos
def agregar_producto(codigo, nombre, precio, stock):

    # Verificar que el código no esté registrado
    if codigo in inventario:
        print("Error: Ya existe un producto con ese código.")
        return

    # Guardar el producto en un diccionario anidado
    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    print("¡Producto agregado correctamente!")


# Función para actualizar el stock
def actualizar_stock(codigo, nuevo_stock):

    # Verificar que el producto exista
    if codigo not in inventario:
        print("Error: No existe un producto con ese código.")
        return

    # Modificar únicamente la cantidad en stock
    inventario[codigo]["stock"] = nuevo_stock

    print("¡Stock actualizado correctamente!")


# Función para buscar un producto por código
def buscar_producto(codigo):

    # Comprobar si el código está registrado
    if codigo not in inventario:
        print("Producto no encontrado.")
        return

    # Obtener todos los detalles del producto
    producto = inventario[codigo]

    print("\nDETALLES DEL PRODUCTO:")
    print(f"Código: {codigo}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock: {producto['stock']}")


# Función para mostrar todos los productos
def mostrar_inventario():

    print("\nINVENTARIO ACTUAL:")

    if not inventario:
        print("No hay productos registrados.")
        return

    for codigo, producto in inventario.items():
        print(
            f"{codigo} - {producto['nombre']} - "
            f"${producto['precio']:.2f} - "
            f"Stock: {producto['stock']}"
        )


# Programa principal
if __name__ == "__main__":

    while True:

        print("\nDESAFÍO 96: GESTIÓN DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Buscar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":

            codigo = input("Código del producto: ").strip().upper()

            if not codigo:
                print("Error: El código no puede estar vacío.")
                continue

            if codigo in inventario:
                print("Error: Ya existe un producto con ese código.")
                continue

            nombre = input("Nombre del producto: ").strip()

            if not nombre:
                print("Error: El nombre no puede estar vacío.")
                continue

            try:
                precio = float(input("Precio del producto: "))
                stock = int(input("Cantidad en stock: "))

                if precio < 0 or stock < 0:
                    print("Error: El precio y el stock no pueden ser negativos.")
                    continue

                agregar_producto(codigo, nombre, precio, stock)

            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "2":

            codigo = input("Código del producto: ").strip().upper()

            if codigo not in inventario:
                print("Error: No existe un producto con ese código.")
                continue

            try:
                nuevo_stock = int(input("Ingrese el nuevo stock: "))

                if nuevo_stock < 0:
                    print("Error: El stock no puede ser negativo.")
                    continue

                actualizar_stock(codigo, nuevo_stock)

            except ValueError:
                print("Error: Debe ingresar un número entero.")

        elif opcion == "3":

            codigo = input("Código del producto: ").strip().upper()
            buscar_producto(codigo)

        elif opcion == "4":

            mostrar_inventario()

        elif opcion == "5":

            print("¡Gracias por utilizar el sistema de inventario!")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")
