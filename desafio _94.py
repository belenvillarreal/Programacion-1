
# Desafío 94: Gestión de usuarios en concursos

# Listas de participantes de cada concurso
astronomia = [
    "ana@1001problemas.com",
    "bruno@1001problemas.com",
    "camila@1001problemas.com",
    "diego@1001problemas.com",
    "emma@1001problemas.com"
]

matematica = [
    "ana@1001problemas.com",
    "camila@1001problemas.com",
    "diego@1001problemas.com",
    "felipe@1001problemas.com",
    "gabriel@1001problemas.com"
]

programacion = [
    "ana@1001problemas.com",
    "camila@1001problemas.com",
    "lucia@1001problemas.com",
    "mateo@1001problemas.com",
    "sofia@1001problemas.com"
]


# Convertir las listas en conjuntos
conjunto_astronomia = set(astronomia)
conjunto_matematica = set(matematica)
conjunto_programacion = set(programacion)


# 1. Usuarios que participaron en los tres concursos
todos_los_concursos = (
    conjunto_astronomia
    & conjunto_matematica
    & conjunto_programacion
)


# 2. Usuarios que participaron solamente en Programación
solo_programacion = (
    conjunto_programacion
    - conjunto_astronomia
    - conjunto_matematica
)


# 3. Usuarios únicos que participaron en al menos un concurso
todos_los_usuarios = (
    conjunto_astronomia
    | conjunto_matematica
    | conjunto_programacion
)


# Mostrar los resultados
print("DESAFÍO 94: GESTIÓN DE USUARIOS EN CONCURSOS")
print()

print("1. USUARIOS QUE PARTICIPARON EN LOS TRES CONCURSOS:")
for usuario in sorted(todos_los_concursos):
    print("-", usuario)

print()
print("2. USUARIOS QUE PARTICIPARON SOLO EN PROGRAMACIÓN:")
for usuario in sorted(solo_programacion):
    print("-", usuario)

print()
print("3. TODOS LOS USUARIOS ÚNICOS:")
for usuario in sorted(todos_los_usuarios):
    print("-", usuario)

print()
print(f"Total de usuarios únicos: {len(todos_los_usuarios)}")
