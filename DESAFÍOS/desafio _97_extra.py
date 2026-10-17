
# Desafío extra: Registro de eventos inmutables

# Lista de eventos: (timestamp, usuario, acción)
eventos = [
    ("2026-10-11 08:00", "Ana", "Inicio de sesión"),
    ("2026-10-11 08:15", "Bruno", "Inicio de sesión"),
    ("2026-10-11 08:30", "Ana", "Consulta"),
    ("2026-10-11 09:00", "Camila", "Inicio de sesión"),
    ("2026-10-11 09:15", "Ana", "Cierre de sesión"),
    ("2026-10-11 09:30", "Bruno", "Consulta"),
    ("2026-10-11 10:00", "Camila", "Consulta"),
    ("2026-10-11 10:15", "Bruno", "Cierre de sesión")
]


# Función para buscar eventos de un usuario
def buscar_eventos_usuario(lista_eventos, usuario_buscado):

    encontrados = []

    for timestamp, usuario, accion in lista_eventos:

        if usuario.lower() == usuario_buscado.lower():
            encontrados.append((timestamp, usuario, accion))

    return encontrados


# Función para contar cuántas veces se realizó cada acción
def contar_acciones(lista_eventos):

    cantidades = {}

    for timestamp, usuario, accion in lista_eventos:

        if accion in cantidades:
            cantidades[accion] += 1
        else:
            cantidades[accion] = 1

    return cantidades


# Programa principal
if __name__ == "__main__":

    print("DESAFÍO EXTRA: REGISTRO DE EVENTOS")
    print()

    # Mostrar todos los eventos registrados
    print("EVENTOS REGISTRADOS:")

    for timestamp, usuario, accion in eventos:
        print(f"{timestamp} | {usuario} | {accion}")

    print()

    # Solicitar un usuario para consultar sus eventos
    usuario_buscado = input(
        "Ingrese el nombre del usuario que desea consultar: "
    ).strip()

    # Buscar los eventos correspondientes
    encontrados = buscar_eventos_usuario(eventos, usuario_buscado)

    print()
    print(f"EVENTOS DEL USUARIO {usuario_buscado.upper()}:")

    if encontrados:
        for timestamp, usuario, accion in encontrados:
            print(f"{timestamp} | {accion}")
    else:
        print("No se encontraron eventos para ese usuario.")

    print()

    # Contar y mostrar las acciones realizadas
    cantidades = contar_acciones(eventos)

    print("CANTIDAD DE VECES QUE SE REALIZÓ CADA ACCIÓN:")

    for accion, cantidad in cantidades.items():
        print(f"{accion}: {cantidad}")
