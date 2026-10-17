
# Desafío 97: Operaciones entre conjuntos de datos

# Conjuntos de usuarios de cada plataforma
facebook = {
    "Ana", "Bruno", "Camila", "Diego", "Emma", "Felipe"
}

instagram = {
    "Ana", "Camila", "Diego", "Gabriel", "Lucia", "Mateo"
}

twitter = {
    "Ana", "Bruno", "Camila", "Lucia", "Sofia", "Valentina"
}


# Función para analizar los conjuntos
def analizar_usuarios(facebook, instagram, twitter):

    # 1. Usuarios que utilizan las tres plataformas
    tres_plataformas = facebook & instagram & twitter

    # 2. Usuarios que utilizan solamente una plataforma
    solo_facebook = facebook - instagram - twitter
    solo_instagram = instagram - facebook - twitter
    solo_twitter = twitter - facebook - instagram

    solo_una = solo_facebook | solo_instagram | solo_twitter

    # 3. Usuarios que utilizan al menos dos plataformas
    al_menos_dos = (
        (facebook & instagram)
        | (facebook & twitter)
        | (instagram & twitter)
    )

    return tres_plataformas, solo_una, al_menos_dos


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 97: ANÁLISIS DE REDES SOCIALES")
    print()

    # Realizar el análisis de los conjuntos
    tres, una, dos_o_mas = analizar_usuarios(
        facebook, instagram, twitter
    )

    # Mostrar usuarios presentes en las tres plataformas
    print("1. USUARIOS QUE UTILIZAN LAS TRES PLATAFORMAS:")

    for usuario in sorted(tres):
        print("-", usuario)

    print()

    # Mostrar usuarios que utilizan solo una plataforma
    print("2. USUARIOS QUE UTILIZAN SOLO UNA PLATAFORMA:")

    for usuario in sorted(una):
        print("-", usuario)

    print()

    # Mostrar usuarios que utilizan al menos dos plataformas
    print("3. USUARIOS QUE UTILIZAN AL MENOS DOS PLATAFORMAS:")

    for usuario in sorted(dos_o_mas):
        print("-", usuario)
