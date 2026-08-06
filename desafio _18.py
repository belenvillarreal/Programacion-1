# Desafío 18: Gestión del Stock de la Verdulería
# Este programa utiliza una lista para representar el inventario
# de una verdulería y responde preguntas sobre los productos almacenados.

print("Desafío 18: Gestión del Stock de la Verdulería")

# Crear la lista con el inventario inicial
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

# Calcular la cantidad de productos del inventario
cantidad_productos = len(inventario)

# Obtener el producto ubicado en la tercera posición
tercer_producto = inventario[2]

# Dejar una línea en blanco para mejorar la presentación
print()

# Mostrar la cantidad de productos
print("Cantidad de productos en el inventario:", cantidad_productos)

# Mostrar el producto ubicado en la tercera posición
print("Producto en la tercera posición:", tercer_producto)