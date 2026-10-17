# Desafío 21: Control de Notas de Estudiantes
# Este programa permite ingresar las notas de una clase,
# calcular el promedio, encontrar la nota más baja y la más alta,
# identificar la nota que más se repite y representar
# las notas mediante un gráfico de barras.

print("Desafío 21: Control de Notas de Estudiantes")

# Importar Counter para contar la frecuencia de las notas
from collections import Counter

# Importar matplotlib para crear el gráfico de barras
import matplotlib.pyplot as plt

# Solicitar al usuario las notas separadas por comas
entrada = input("Ingrese las notas separadas por comas: ")

# Convertir la entrada en una lista de números
notas = []

for nota in entrada.split(","):
    notas.append(float(nota))

# -----------------------------
# Pregunta 1
# -----------------------------

# Calcular el promedio
promedio = sum(notas) / len(notas)

print()
print("Pregunta 1:")
print("El promedio de la clase es:", promedio)

# -----------------------------
# Pregunta 2
# -----------------------------

# Buscar la nota mínima y máxima
nota_minima = min(notas)
nota_maxima = max(notas)

print()
print("Pregunta 2:")
print("La nota más baja es:", nota_minima)
print("La nota más alta es:", nota_maxima)

# -----------------------------
# Pregunta 3
# -----------------------------

# Contar cuántas veces aparece cada nota
contador = Counter(notas)

# Obtener la nota más repetida
nota_mas_repetida = contador.most_common(1)

print()
print("Pregunta 3:")
print("La nota que más se repite es:", nota_mas_repetida[0][0])
print("Cantidad de veces:", nota_mas_repetida[0][1])

# -----------------------------
# Pregunta 4
# -----------------------------

# Crear un gráfico de barras
plt.figure(figsize=(8,5))

plt.bar(range(len(notas)), notas)

plt.title("Notas de los estudiantes")

plt.xlabel("Estudiantes")

plt.ylabel("Notas")

plt.show()