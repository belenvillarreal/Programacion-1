
# Desafío extra: Encontrar el mayor de tres números

print("DESAFÍO EXTRA: NÚMERO MAYOR")
print()

# Solicitar tres números enteros al usuario
try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))

    # Comprobar si los tres números son iguales
    if numero1 == numero2 == numero3:
        print("Los tres números son iguales.")

    # Determinar cuál es el número mayor
    else:
        mayor = max(numero1, numero2, numero3)
        print(f"El número mayor es: {mayor}")

except ValueError:
    print("Error: Debe ingresar números enteros válidos.")
