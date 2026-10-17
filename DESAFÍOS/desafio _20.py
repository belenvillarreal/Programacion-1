print("Desafío 20: Caracteres ASCII")

# Crear una lista de números ASCII
numeros_ascii = [72, 79, 76, 65, 33]

# Crear una lista vacía para guardar los caracteres convertidos
caracteres = []

print("Lista de números ASCII:")
print(numeros_ascii)

print()

print("Conversión de números a caracteres:")

# Recorrer la lista una sola vez
for numero in numeros_ascii:

    # Convertir el número a carácter usando chr()
    caracter = chr(numero)

    # Guardar el carácter en la lista
    caracteres.append(caracter)

    # Mostrar la conversión
    print(numero, "->", caracter)

print()

# Unir los caracteres para formar un mensaje
mensaje = "".join(caracteres)

print("Mensaje formado:")
print(mensaje)
