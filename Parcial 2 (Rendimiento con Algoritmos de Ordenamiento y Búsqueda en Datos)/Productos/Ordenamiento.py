from Productos.Generar import Producto
from typing import List, Callable
import time

# Parte 2: Algoritmos de Ordenamiento
def ordenamiento_mezcla(arr: List[Producto], key_func: Callable, reverso: bool = False) -> List[Producto]:
    """Implementación del algoritmo Merge Sort."""
    # Crear una copia para no modificar el original
    arr_copia = arr.copy()

    # Arreglo auxiliar para evitar crear nuevos arreglos en cada mezcla
    aux = [None] * len(arr_copia)

    def mezclar(inicio, medio, fin):
        # Copiar elementos a arreglo auxiliar
        for k in range(inicio, fin + 1):
            aux[k] = arr_copia[k]

        i, j = inicio, medio + 1
        for k in range(inicio, fin + 1):
            if i > medio:
                arr_copia[k] = aux[j]
                j += 1
            elif j > fin:
                arr_copia[k] = aux[i]
                i += 1
            elif (key_func(aux[i]) < key_func(aux[j])) != reverso:
                arr_copia[k] = aux[i]
                i += 1
            else:
                arr_copia[k] = aux[j]
                j += 1

    def ordenar(inicio, fin):
        if fin <= inicio:
            return
        medio = (inicio + fin) // 2
        ordenar(inicio, medio)
        ordenar(medio + 1, fin)
        mezclar(inicio, medio, fin)

    ordenar(0, len(arr_copia) - 1)
    return arr_copia


def ordenamiento_rapido(arr: List[Producto], key_func: Callable, reverso: bool = False) -> List[Producto]:
    """Implementación del algoritmo Quick Sort."""

    # Crear una copia para no modificar el original
    arr_copia = arr.copy()

    def particion(inicio, fin):
        # Selección de pivote (mediana de tres)
        medio = (inicio + fin) // 2
        # Ordenar inicio, medio, fin
        if key_func(arr_copia[inicio]) > key_func(arr_copia[medio]):
            arr_copia[inicio], arr_copia[medio] = arr_copia[medio], arr_copia[inicio]
        if key_func(arr_copia[medio]) > key_func(arr_copia[fin]):
            arr_copia[medio], arr_copia[fin] = arr_copia[fin], arr_copia[medio]
        if key_func(arr_copia[inicio]) > key_func(arr_copia[medio]):
            arr_copia[inicio], arr_copia[medio] = arr_copia[medio], arr_copia[inicio]

        # Usar el elemento del medio como pivote
        pivote = key_func(arr_copia[medio])

        # Mover el pivote al final
        arr_copia[medio], arr_copia[fin - 1] = arr_copia[fin - 1], arr_copia[medio]

        # Índices para partición
        i, j = inicio, fin - 1

        while True:
            i += 1
            while key_func(arr_copia[i]) < pivote:
                i += 1
            j -= 1
            while key_func(arr_copia[j]) > pivote:
                j -= 1
            if i >= j:
                break
            arr_copia[i], arr_copia[j] = arr_copia[j], arr_copia[i]

        # Restaurar pivote
        arr_copia[i], arr_copia[fin - 1] = arr_copia[fin - 1], arr_copia[i]
        return i

    def ordenamiento_insercion(inicio, fin):
        for i in range(inicio + 1, fin + 1):
            elemento = arr_copia[i]
            valor_clave = key_func(elemento)
            j = i - 1
            while j >= inicio and (key_func(arr_copia[j]) > valor_clave) != reverso:
                arr_copia[j + 1] = arr_copia[j]
                j -= 1
            arr_copia[j + 1] = elemento

    def ordenar(inicio, fin):
        # Usar ordenamiento por inserción para subarreglos pequeños
        if fin - inicio < 10:
            ordenamiento_insercion(inicio, fin)
            return

        if inicio < fin:
            # Invertir comparaciones si es reverso
            if reverso:
                # Implementación para orden inverso
                pass

            indice_pivote = particion(inicio, fin)

            # Revertir el intercambio después de la partición si es reverso
            if reverso:
                # Implementación para orden inverso
                pass

            ordenar(inicio, indice_pivote - 1)
            ordenar(indice_pivote + 1, fin)

    ordenar(0, len(arr_copia) - 1)
    return arr_copia


def ordenamiento_insercion(arr: List[Producto], key_func: Callable, reverso: bool = False) -> List[Producto]:
    """Implementación del algoritmo Insertion Sort."""
    arr_copia = arr.copy()

    for i in range(1, len(arr_copia)):
        elemento_clave = arr_copia[i]
        valor_clave = key_func(elemento_clave)
        j = i - 1

        # Optimización: Mover elementos en un solo paso
        while j >= 0 and (key_func(arr_copia[j]) > valor_clave) != reverso:
            arr_copia[j + 1] = arr_copia[j]
            j -= 1

        arr_copia[j + 1] = elemento_clave

    return arr_copia

def medir_tiempo_ordenamiento(func_ordenamiento, productos, key_func, reverso=False, repeticiones=10):
    """Mide el tiempo que tarda un algoritmo de ordenamiento"""
    tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        productos_ordenados = func_ordenamiento(productos, key_func, reverso)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # Tiempo en milisegundos

    tiempo_promedio = sum(tiempos) / len(tiempos)
    return tiempo_promedio, productos_ordenados