
# Desafío 101: Historial médico inmutable

# Lista de registros médicos
# Cada registro es una tupla: (fecha, paciente, diagnóstico)
registros_medicos = [
    ("2026-01-10", "Ana", "Gripe"),
    ("2026-01-15", "Bruno", "Alergia"),
    ("2026-02-05", "Camila", "Resfriado"),
    ("2026-02-20", "Ana", "Dolor de cabeza"),
    ("2026-03-10", "Bruno", "Gripe"),
    ("2026-03-25", "Ana", "Alergia"),
    ("2026-04-12", "Camila", "Gripe"),
    ("2026-05-08", "Diego", "Resfriado")
]


# Función para consultar el historial de un paciente
def consultar_historial(registros, paciente_buscado):

    historial = []

    # Recorrer todos los registros médicos
    for fecha, paciente, diagnostico in registros:

        # Comparar el nombre sin distinguir mayúsculas
        if paciente.lower() == paciente_buscado.lower():

            # Guardar el registro completo del paciente
            historial.append((fecha, paciente, diagnostico))

    return historial


# Función para contar diagnósticos distintos
def contar_diagnosticos_distintos(registros):

    # Conjunto para almacenar diagnósticos sin repetir
    diagnosticos = set()

    for fecha, paciente, diagnostico in registros:
        diagnosticos.add(diagnostico)

    return diagnosticos


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO 101: HISTORIAL MÉDICO INMUTABLE")
    print()

    # Mostrar todos los registros almacenados
    print("REGISTROS MÉDICOS ALMACENADOS:")

    for fecha, paciente, diagnostico in registros_medicos:
        print(f"{fecha} | {paciente} | {diagnostico}")

    print()

    # Solicitar el nombre del paciente
    paciente_buscado = input(
        "Ingrese el nombre del paciente a consultar: "
    ).strip()

    # Buscar el historial del paciente
    historial = consultar_historial(
        registros_medicos, paciente_buscado
    )

    print()
    print(f"HISTORIAL MÉDICO DE {paciente_buscado.upper()}:")

    if historial:

        for fecha, paciente, diagnostico in historial:
            print(f"Fecha: {fecha}")
            print(f"Diagnóstico: {diagnostico}")
            print()

    else:
        print("No se encontraron registros para ese paciente.")

    # Obtener los diagnósticos distintos
    diagnosticos = contar_diagnosticos_distintos(
        registros_medicos
    )

    # Mostrar la cantidad de diagnósticos diferentes
    print()
    print("DIAGNÓSTICOS DISTINTOS REGISTRADOS:")

    for diagnostico in sorted(diagnosticos):
        print("-", diagnostico)

    print()
    print(f"Cantidad total de diagnósticos distintos: {len(diagnosticos)}")
