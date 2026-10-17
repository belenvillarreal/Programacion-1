
# Desafío 98: Plataforma educativa en línea

# Conjunto de cursos ofrecidos por la plataforma
cursos_ofrecidos = {
    "Python",
    "Matemática",
    "Robótica",
    "Inglés"
}

# Diccionario de estudiantes y cursos completados
# Cada estudiante tiene un conjunto de cursos
estudiantes = {
    "Ana": {"Python", "Matemática", "Robótica", "Inglés"},
    "Bruno": {"Python", "Matemática"},
    "Camila": {"Python"},
    "Diego": {"Robótica"},
    "Emma": {"Python", "Matemática", "Robótica", "Inglés"},
    "Felipe": {"Inglés", "Robótica"},
    "Lucia": {"Python"},
    "Mateo": {"Matemática"}
}


# Función para registrar cursos completados
def registrar_curso(nombre, curso):

    # Verificar que el curso exista
    if curso not in cursos_ofrecidos:
        print("Error: El curso no está disponible.")
        return

    # Si el estudiante no existe, crear su registro
    if nombre not in estudiantes:
        estudiantes[nombre] = set()

    # Agregar el curso al conjunto del estudiante
    estudiantes[nombre].add(curso)

    print("¡Curso registrado correctamente!")


# Función para encontrar estudiantes que completaron todos los cursos
def estudiantes_todos_los_cursos():

    completaron_todos = []

    for nombre, cursos in estudiantes.items():

        if cursos_ofrecidos.issubset(cursos):
            completaron_todos.append(nombre)

    return completaron_todos


# Función para encontrar estudiantes que completaron solo un curso
def estudiantes_solo_un_curso(curso_buscado):

    resultado = []

    for nombre, cursos in estudiantes.items():

        # El conjunto debe contener únicamente el curso solicitado
        if cursos == {curso_buscado}:
            resultado.append(nombre)

    return resultado


# Programa principal
if __name__ == "__main__":

    while True:

        print("\nDESAFÍO 98: PLATAFORMA EDUCATIVA")
        print("1. Registrar curso completado")
        print("2. Ver estudiantes que completaron todos los cursos")
        print("3. Buscar estudiantes que solo completaron un curso")
        print("4. Mostrar estudiantes y cursos")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":

            nombre = input("Nombre del estudiante: ").strip().title()
            curso = input("Curso completado: ").strip()

            if not nombre:
                print("Error: El nombre no puede estar vacío.")
            else:
                registrar_curso(nombre, curso)

        elif opcion == "2":

            resultado = estudiantes_todos_los_cursos()

            print("\nESTUDIANTES QUE COMPLETARON TODOS LOS CURSOS:")

            if resultado:
                for nombre in sorted(resultado):
                    print("-", nombre)
            else:
                print("Ningún estudiante completó todos los cursos.")

        elif opcion == "3":

            curso = input("Ingrese el curso que desea consultar: ").strip()

            if curso not in cursos_ofrecidos:
                print("Error: El curso no está disponible.")
                continue

            resultado = estudiantes_solo_un_curso(curso)

            print(f"\nESTUDIANTES QUE SOLO COMPLETARON {curso}:")

            if resultado:
                for nombre in sorted(resultado):
                    print("-", nombre)
            else:
                print("No se encontraron estudiantes.")

        elif opcion == "4":

            print("\nESTUDIANTES Y CURSOS COMPLETADOS:")

            for nombre, cursos in sorted(estudiantes.items()):
                print(f"{nombre}: {', '.join(sorted(cursos))}")

        elif opcion == "5":

            print("¡Gracias por utilizar la plataforma educativa!")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")
