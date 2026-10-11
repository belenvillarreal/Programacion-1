
# Desafío 93: Traductor multilingüe mejorado

# Diccionario de palabras en inglés y sus traducciones
traducciones = {
    "hello": {
        "es": "hola",
        "fr": "bonjour",
        "it": "ciao",
        "de": "hallo",
        "pt": "olá"
    },
    "goodbye": {
        "es": "adiós",
        "fr": "au revoir",
        "it": "arrivederci",
        "de": "auf wiedersehen",
        "pt": "adeus"
    },
    "book": {
        "es": "libro",
        "fr": "livre",
        "it": "libro",
        "de": "buch",
        "pt": "livro"
    },
    "house": {
        "es": "casa",
        "fr": "maison",
        "it": "casa",
        "de": "haus",
        "pt": "casa"
    },
    "water": {
        "es": "agua",
        "fr": "eau",
        "it": "acqua",
        "de": "wasser",
        "pt": "água"
    },
    "school": {
        "es": "escuela",
        "fr": "école",
        "it": "scuola",
        "de": "schule",
        "pt": "escola"
    },
    "friend": {
        "es": "amigo",
        "fr": "ami",
        "it": "amico",
        "de": "freund",
        "pt": "amigo"
    },
    "computer": {
        "es": "computadora",
        "fr": "ordinateur",
        "it": "computer",
        "de": "computer",
        "pt": "computador"
    }
}


# Función para traducir una palabra a varios idiomas
def traducir_palabra(palabra, idiomas):

    # Diccionario para guardar los resultados
    resultados = {}

    # Buscar la palabra en el diccionario principal
    if palabra not in traducciones:

        for idioma in idiomas:
            resultados[idioma] = "Traducción no encontrada"

        return resultados

    # Recorrer los idiomas solicitados
    for idioma in idiomas:

        # Buscar la traducción correspondiente
        traduccion = traducciones[palabra].get(
            idioma, "Traducción no encontrada"
        )

        # Guardar el resultado
        resultados[idioma] = traduccion

    return resultados


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 93: TRADUCTOR MULTILINGÜE")
    print()

    # Mostrar los idiomas disponibles
    print("IDIOMAS DISPONIBLES:")
    print("es = Español")
    print("fr = Francés")
    print("it = Italiano")
    print("de = Alemán")
    print("pt = Portugués")
    print()

    # Solicitar una palabra en inglés
    palabra = input("Ingrese una palabra en inglés: ").strip().lower()

    # Solicitar los idiomas separados por comas
    entrada = input(
        "Ingrese los idiomas separados por comas (ej: es,it,de): "
    )

    # Convertir la entrada en una lista de idiomas
    idiomas = [
        idioma.strip().lower()
        for idioma in entrada.split(",")
        if idioma.strip()
    ]

    # Llamar a la función de traducción
    resultados = traducir_palabra(palabra, idiomas)

    # Mostrar las traducciones encontradas
    print()
    print(f"TRADUCCIONES DE '{palabra}':")

    for idioma, traduccion in resultados.items():
        print(f"{idioma}: {traduccion}")
