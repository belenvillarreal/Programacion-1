print ("Desafio 20 Caracteres ASCII")
# Pedir al usuario una lista de números separados por espacios
entrada = input("Ingresa números ASCII separados por espacios: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split()))

# Transformar a caracteres
caracteres = [chr(n) for n in numeros]

print("Caracteres:", caracteres)
