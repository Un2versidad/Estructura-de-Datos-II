from collections import deque

def problema_jarras_agua():
    # Capacidades de las jarras
    capacidad_jarra_4 = 4
    capacidad_jarra_3 = 3
    objetivo = 2

    # Estados visitados
    visitados = set()

    # Cola para BFS: (jarra_4, jarra_3, pasos)
    cola = deque([(0, 0, [])])

    while cola:
        jarra_4, jarra_3, pasos = cola.popleft()

        # Si llegamos a la meta
        if jarra_4 == objetivo:
            return pasos

        # Evitar estados repetidos
        estado = (jarra_4, jarra_3)
        if estado in visitados:
            continue
        visitados.add(estado)

        # Todas las operaciones posibles:

        # 1. Llenar jarra de 4 galones
        if jarra_4 < capacidad_jarra_4:
            cola.append((capacidad_jarra_4, jarra_3, pasos + [f"Llenar jarra de 4 galones: ({capacidad_jarra_4}, {jarra_3})"]))

        # 2. Llenar jarra de 3 galones
        if jarra_3 < capacidad_jarra_3:
            cola.append((jarra_4, capacidad_jarra_3, pasos + [f"Llenar jarra de 3 galones: ({jarra_4}, {capacidad_jarra_3})"]))

        # 3. Vaciar jarra de 4 galones
        if jarra_4 > 0:
            cola.append((0, jarra_3, pasos + [f"Vaciar jarra de 4 galones: (0, {jarra_3})"]))

        # 4. Vaciar jarra de 3 galones
        if jarra_3 > 0:
            cola.append((jarra_4, 0, pasos + [f"Vaciar jarra de 3 galones: ({jarra_4}, 0)"]))

        # 5. Verter de jarra 4 a jarra 3
        if jarra_4 > 0 and jarra_3 < capacidad_jarra_3:
            vertido = min(jarra_4, capacidad_jarra_3 - jarra_3)
            cola.append((jarra_4 - vertido, jarra_3 + vertido,
                          pasos + [f"Verter de jarra 4 a jarra 3: ({jarra_4 - vertido}, {jarra_3 + vertido})"]))

        # 6. Verter de jarra 3 a jarra 4
        if jarra_3 > 0 and jarra_4 < capacidad_jarra_4:
            vertido = min(jarra_3, capacidad_jarra_4 - jarra_4)
            cola.append((jarra_4 + vertido, jarra_3 - vertido,
                          pasos + [f"Verter de jarra 3 a jarra 4: ({jarra_4 + vertido}, {jarra_3 - vertido})"]))

    return "No hay solución"

if __name__ == "__main__":
    print("Solución al problema de las jarras:")
    pasos = problema_jarras_agua()
    for i, paso in enumerate(pasos, 1):
        print(f"Paso {i}: {paso}")