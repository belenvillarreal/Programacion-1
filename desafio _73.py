
# Desafío 73: Eliminar elementos duplicados de una lista

def eliminar_duplicados(numeros):
    """
    Elimina los elementos repetidos de una lista,
    conservando una sola aparición de cada número
    y respetando el orden original.
    """
    lista_sin_duplicados = []

    # Recorrer cada número de la lista original
    for numero in numeros:
        # Agregarlo solamente si todavía no aparece
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)

    return lista_sin_duplicados


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 73: ELIMINAR ELEMENTOS DUPLICADOS")
    print()

    # Lista original con números repetidos
    lista_original = [5, 8, 3, 5, 2, 8, 9, 3, 1, 2, 7]

    # Obtener una nueva lista sin elementos duplicados
    lista_sin_duplicados = eliminar_duplicados(lista_original)

    # Mostrar ambas listas claramente
    print("Lista original:", lista_original)
    print("Lista sin duplicados:", lista_sin_duplicados)
