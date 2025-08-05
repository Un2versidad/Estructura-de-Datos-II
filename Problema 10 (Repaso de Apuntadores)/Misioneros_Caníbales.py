from collections import deque

def misioneros_canibales():
    # Estado: (m_izq, c_izq, bote, m_der, c_der)
    inicial = (3, 3, 1, 0, 0)  # Todos en la izquierda, bote en izquierda
    meta = (0, 0, 0, 3, 3)     # Todos en la derecha, bote en derecha

    visitados = set()
    cola = deque([(inicial, [])])

    while cola:
        estado, camino = cola.popleft()
        m_izq, c_izq, bote, m_der, c_der = estado

        if estado == meta:
            return camino

        if estado in visitados:
            continue

        visitados.add(estado)

        # Generar movimientos válidos
        if bote == 1:  # Bote en la izquierda (->)
            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2 and m <= m_izq and c <= c_izq:
                        nuevo_m_izq = m_izq - m
                        nuevo_c_izq = c_izq - c
                        nuevo_m_der = m_der + m
                        nuevo_c_der = c_der + c

                        # Verificar si el estado es seguro
                        if ((nuevo_m_izq == 0 or nuevo_m_izq >= nuevo_c_izq) and
                            (nuevo_m_der == 0 or nuevo_m_der >= nuevo_c_der)):
                            nuevo_estado = (nuevo_m_izq, nuevo_c_izq, 0, nuevo_m_der, nuevo_c_der)
                            movimiento = f"{m}M {c}C izquierda->derecha: {nuevo_estado}"
                            cola.append((nuevo_estado, camino + [movimiento]))
        else:  # Bote en la derecha (<-)
            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2 and m <= m_der and c <= c_der:
                        nuevo_m_izq = m_izq + m
                        nuevo_c_izq = c_izq + c
                        nuevo_m_der = m_der - m
                        nuevo_c_der = c_der - c

                        # Verificar si el estado es seguro
                        if ((nuevo_m_izq == 0 or nuevo_m_izq >= nuevo_c_izq) and
                            (nuevo_m_der == 0 or nuevo_m_der >= nuevo_c_der)):
                            nuevo_estado = (nuevo_m_izq, nuevo_c_izq, 1, nuevo_m_der, nuevo_c_der)
                            movimiento = f"{m}M {c}C derecha->izquierda: {nuevo_estado}"
                            cola.append((nuevo_estado, camino + [movimiento]))

    return "No hay solución"

if __name__ == "__main__":
    print("Solución al problema de misioneros y caníbales:")
    pasos = misioneros_canibales()
    for i, paso in enumerate(pasos, 1):
        print(f"Paso {i}: {paso}")