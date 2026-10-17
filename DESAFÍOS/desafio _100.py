
# Desafío 100: Análisis deportivo con conjuntos

# Conjuntos de atletas que participaron en cada torneo
torneo_1 = {
    "Ana", "Bruno", "Camila", "Diego", "Emma", "Felipe"
}

torneo_2 = {
    "Ana", "Camila", "Diego", "Gabriel", "Lucia", "Mateo"
}

torneo_3 = {
    "Ana", "Bruno", "Camila", "Lucia", "Sofia", "Valentina"
}


# Función para identificar atletas de todos los torneos
def atletas_todos_los_torneos(torneos):

    # Intersección de todos los conjuntos
    resultado = set.intersection(*torneos)

    return resultado


# Función para identificar atletas de un único torneo
def atletas_unico_torneo(torneos):

    # Contar en cuántos torneos participó cada atleta
    participaciones = {}

    for torneo in torneos:
        for atleta in torneo:

            if atleta in participaciones:
                participaciones[atleta] += 1
            else:
                participaciones[atleta] = 1

    # Seleccionar quienes participaron en un solo torneo
    exclusivos = set()

    for atleta, cantidad in participaciones.items():
        if cantidad == 1:
            exclusivos.add(atleta)

    return exclusivos


# Función para obtener todos los atletas únicos
def obtener_atletas_unicos(torneos):

    # Unir los conjuntos sin repetir atletas
    atletas_unicos = set.union(*torneos)

    return atletas_unicos


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 100: ANÁLISIS DEPORTIVO")
    print()

    # Agrupar los conjuntos de torneos
    torneos = [torneo_1, torneo_2, torneo_3]

    # Realizar los cálculos
    todos = atletas_todos_los_torneos(torneos)
    exclusivos = atletas_unico_torneo(torneos)
    unicos = obtener_atletas_unicos(torneos)

    # Mostrar los atletas que participaron en todos los torneos
    print("1. ATLETAS QUE PARTICIPARON EN TODOS LOS TORNEOS:")

    for atleta in sorted(todos):
        print("-", atleta)

    print()

    # Mostrar los atletas de un único torneo
    print("2. ATLETAS QUE PARTICIPARON EN UN ÚNICO TORNEO:")

    for atleta in sorted(exclusivos):
        print("-", atleta)

    print()

    # Mostrar todos los atletas únicos
    print("3. TODOS LOS ATLETAS ÚNICOS:")

    for atleta in sorted(unicos):
        print("-", atleta)

    print()

    # Mostrar la cantidad total
    print(f"Cantidad total de atletas únicos: {len(unicos)}")
