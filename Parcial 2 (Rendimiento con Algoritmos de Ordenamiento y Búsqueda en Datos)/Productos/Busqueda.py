from colorama import Fore
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
from Productos.Generar import Producto
import time

# Parte 3: Funciones de Búsqueda

# Búsqueda Binaria
def busqueda_binaria(productos: List[Producto], id_objetivo: int) -> Optional[Producto]:
    """Implementación de búsqueda binaria por ID."""
    izquierda, derecha = 0, len(productos) - 1

    while izquierda <= derecha:
        # Cálculo de punto medio optimizado para evitar desbordamiento
        medio = izquierda + (derecha - izquierda) // 2

        if productos[medio].id == id_objetivo:
            return productos[medio]
        elif productos[medio].id < id_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None

def busqueda_lineal_por_nombre(productos: List[Producto], subcadena_nombre: str) -> List[Producto]:
    """Implementa búsqueda lineal por subcadena en el nombre."""
    return [p for p in productos if subcadena_nombre.lower() in p.nombre.lower()]

# Búsqueda Lineal Paralela
def busqueda_lineal_paralela(productos: List[Producto], subcadena_nombre: str) -> List[Producto]:
    """Búsqueda lineal con procesamiento paralelo."""
    subcadena = subcadena_nombre.lower()  # Convertir a minúsculas una sola vez

    def buscar_en_bloque(bloque):
        return [p for p in bloque if subcadena in p.nombre.lower()]

    # Para listas pequeñas, usar búsqueda secuencial
    if len(productos) < 500:
        return [p for p in productos if subcadena in p.nombre.lower()]

    # Para listas más grandes, usar paralelismo
    num_hilos = min(8, len(productos) // 200 + 1)
    tamanio_bloque = len(productos) // num_hilos
    bloques = [productos[i:i + tamanio_bloque] for i in range(0, len(productos), tamanio_bloque)]

    resultados = []
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        for resultado in executor.map(buscar_en_bloque, bloques):
            resultados.extend(resultado)

    return resultados

# Implementación de Trie para búsqueda por subcadenas
class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.indices_productos = set()

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, texto, indice_producto):
        """Inserta todas las subcadenas del texto en el trie."""
        texto = texto.lower()
        # Insertar todas las subcadenas para búsqueda eficiente
        for i in range(len(texto)):
            nodo = self.raiz
            for j in range(i, len(texto)):
                char = texto[j]
                if char not in nodo.hijos:
                    nodo.hijos[char] = NodoTrie()
                nodo = nodo.hijos[char]
                nodo.indices_productos.add(indice_producto)

    def buscar(self, subcadena):
        """Busca productos que contengan la subcadena."""
        subcadena = subcadena.lower()
        nodo = self.raiz
        for char in subcadena:
            if char not in nodo.hijos:
                return set()
            nodo = nodo.hijos[char]
        return nodo.indices_productos

def construir_indice_trie(productos):
    """Construye un índice trie para los nombres de productos."""
    trie = Trie()
    for i, producto in enumerate(productos):
        trie.insertar(producto.nombre, i)
    return trie

def busqueda_trie(productos, trie, subcadena):
    """Busca productos usando el índice trie."""
    indices = trie.buscar(subcadena.lower())
    return [productos[i] for i in indices]

# Sistema de caché para búsquedas frecuentes
class CacheBusqueda:
    def __init__(self, capacidad=100):
        self.capacidad = capacidad
        self.cache = {}
        self.uso = {}
        self.contador = 0

    def obtener(self, clave):
        if clave in self.cache:
            self.uso[clave] = self.contador
            self.contador += 1
            return self.cache[clave]
        return None

    def guardar(self, clave, valor):
        if len(self.cache) >= self.capacidad:
            # Eliminar el elemento menos usado
            min_clave = min(self.uso.items(), key=lambda x: x[1])[0]
            del self.cache[min_clave]
            del self.uso[min_clave]

        self.cache[clave] = valor
        self.uso[clave] = self.contador
        self.contador += 1

# Sistema de búsqueda
class SistemaBusqueda:
    def __init__(self, productos):
        self.productos = productos
        self.ordenados_por_id = None
        self.indice_trie = None
        self.cache = CacheBusqueda()

    def preparar_indices(self):
        """Prepara los índices necesarios para búsquedas eficientes."""
        print(f"{Fore.YELLOW}Preparando índices para búsquedas...")

        # Ordenar por ID para búsqueda binaria
        inicio = time.perf_counter()
        self.ordenados_por_id = sorted(self.productos, key=lambda p: p.id)
        fin = time.perf_counter()
        print(f"{Fore.GREEN}✓ Productos ordenados por ID en {(fin - inicio) * 1000:.2f} ms")

        # Construir índice trie para búsqueda por nombre
        inicio = time.perf_counter()
        self.indice_trie = construir_indice_trie(self.productos)
        fin = time.perf_counter()
        print(f"{Fore.GREEN}✓ Índice trie construido en {(fin - inicio) * 1000:.2f} ms")

    def buscar_por_id(self, id_objetivo):
        """Búsqueda por ID."""
        clave_cache = f"id:{id_objetivo}"
        resultado = self.cache.obtener(clave_cache)
        if resultado is not None:
            return resultado

        if self.ordenados_por_id is None:
            self.ordenados_por_id = sorted(self.productos, key=lambda p: p.id)

        resultado = busqueda_binaria(self.ordenados_por_id, id_objetivo)
        self.cache.guardar(clave_cache, resultado)
        return resultado

    def buscar_por_nombre(self, subcadena, metodo="auto"):
        """Búsqueda por nombre con selección automática del mejor método."""
        clave_cache = f"nombre:{subcadena.lower()}:{metodo}"
        resultado = self.cache.obtener(clave_cache)
        if resultado is not None:
            return resultado

        if metodo == "auto":
            # Elegir el mejor método según características de la búsqueda
            if len(self.productos) > 1000 and len(subcadena) >= 3:
                if self.indice_trie is None:
                    self.indice_trie = construir_indice_trie(self.productos)
                resultado = busqueda_trie(self.productos, self.indice_trie, subcadena)
            else:
                resultado = busqueda_lineal_paralela(self.productos, subcadena)
        elif metodo == "trie":
            if self.indice_trie is None:
                self.indice_trie = construir_indice_trie(self.productos)
            resultado = busqueda_trie(self.productos, self.indice_trie, subcadena)
        elif metodo == "paralelo":
            resultado = busqueda_lineal_paralela(self.productos, subcadena)
        else:  # Método estándar
            resultado = [p for p in self.productos if subcadena.lower() in p.nombre.lower()]

        self.cache.guardar(clave_cache, resultado)
        return resultado

    def comparar_metodos_busqueda(self, subcadenas):
        """Compara el rendimiento de diferentes métodos de búsqueda."""
        resultados = {
            "Lineal Estándar": [],
            "Lineal Paralelo": [],
            "Trie": []
        }

        for subcadena in subcadenas:
            print(f"\n{Fore.CYAN}Probando búsqueda para '{subcadena}':")

            # Búsqueda lineal estándar
            tiempos = []
            for _ in range(5):
                inicio = time.perf_counter()
                res1 = [p for p in self.productos if subcadena.lower() in p.nombre.lower()]
                fin = time.perf_counter()
                tiempos.append((fin - inicio) * 1000)
            t1 = sum(tiempos) / len(tiempos)
            resultados["Lineal Estándar"].append((t1, len(res1)))
            print(f"{Fore.WHITE}Lineal Estándar: {Fore.GREEN}{t1:.4f} ms ({len(res1)} resultados)")

            # Búsqueda lineal paralela
            tiempos = []
            for _ in range(5):
                inicio = time.perf_counter()
                res2 = busqueda_lineal_paralela(self.productos, subcadena)
                fin = time.perf_counter()
                tiempos.append((fin - inicio) * 1000)
            t2 = sum(tiempos) / len(tiempos)
            resultados["Lineal Paralelo"].append((t2, len(res2)))
            print(f"{Fore.WHITE}Lineal Paralelo: {Fore.GREEN}{t2:.4f} ms ({len(res2)} resultados)")

            # Búsqueda con trie
            if self.indice_trie is None:
                self.indice_trie = construir_indice_trie(self.productos)
            tiempos = []
            for _ in range(5):
                inicio = time.perf_counter()
                indices = self.indice_trie.buscar(subcadena)
                res3 = [self.productos[i] for i in indices]
                fin = time.perf_counter()
                tiempos.append((fin - inicio) * 1000)
            t3 = sum(tiempos) / len(tiempos)
            resultados["Trie"].append((t3, len(res3)))
            print(f"{Fore.WHITE}Trie: {Fore.GREEN}{t3:.4f} ms ({len(res3)} resultados)")

        return resultados