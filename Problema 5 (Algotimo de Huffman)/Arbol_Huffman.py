import heapq
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol(simbolos, frecuencias):
    heap = []
    for s, f in zip(simbolos, frecuencias):
        heapq.heappush(heap, Nodo(s, f))
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        nuevo = Nodo(None, n1.frecuencia + n2.frecuencia)
        nuevo.izquierda = n1
        nuevo.derecha = n2
        heapq.heappush(heap, nuevo)
    return heap[0]

def recorrer_interactivo(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return
    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = codigo_actual
        print(Fore.GREEN + f"\n🌟 Nodo hoja encontrado: '{nodo.simbolo}' con código: {codigo_actual}")
        input(Fore.YELLOW + "Presiona ENTER para continuar...")
    else:
        print(Fore.CYAN + f"\nRama intermedia con frecuencia total: {nodo.frecuencia}")
        print(Fore.CYAN + ascii_art(codigo_actual))
        input(Fore.YELLOW + "Presiona ENTER para continuar explorando...")
    recorrer_interactivo(nodo.izquierda, codigo_actual + "0", codigos)
    recorrer_interactivo(nodo.derecha, codigo_actual + "1", codigos)
    return codigos

def ascii_art(ruta):
    """
    Dibujo ascii-art aproximado de la ruta binaria explorada
    """
    if not ruta:
        return "[raíz]"
    dibujo = ""
    for bit in ruta:
        if bit == "0":
            dibujo += " └─0→ "
        else:
            dibujo += " └─1→ "
    return dibujo

def mostrar_codigos(codigos, frecuencias):
    tabla = []
    for simbolo, codigo in codigos.items():
        tabla.append([simbolo, frecuencias[simbolo], codigo])
    print("\n" + Fore.GREEN + Style.BRIGHT + "Códigos de Huffman generados:\n")
    print(tabulate(tabla, headers=["Símbolo", "Frecuencia", "Código Huffman"], tablefmt="fancy_grid"))

def pedir_datos():
    simbolos = []
    frecuencias = {}
    while True:
        try:
            n = int(input(Fore.CYAN + "¿Cuántos símbolos vas a ingresar? "))
            if n <= 0:
                raise ValueError("Debe ser mayor que cero.")
            break
        except ValueError as e:
            print(Fore.RED + f"Entrada inválida: {e}")
    for i in range(n):
        while True:
            s = input(Fore.YELLOW + f"Ingrese símbolo #{i+1}: ").strip()
            if len(s) != 1 or not s.isprintable():
                print(Fore.RED + "Símbolo inválido, ingrese un carácter único imprimible.")
                continue
            if s in simbolos:
                print(Fore.RED + "Símbolo duplicado, ingrese otro distinto.")
                continue
            break
        while True:
            try:
                f = int(input(Fore.YELLOW + f"Ingrese frecuencia para {s}: "))
                if f <= 0:
                    raise ValueError("La frecuencia debe ser positiva.")
                break
            except ValueError as e:
                print(Fore.RED + f"Frecuencia inválida: {e}")
        simbolos.append(s)
        frecuencias[s] = f
    return simbolos, frecuencias

if __name__ == "__main__":
    print(Fore.MAGENTA + Style.BRIGHT + "\n*** Codificador de Huffman interactivo con recorrido paso a paso ***\n")

    simbolos, frecs_dict = pedir_datos()
    frecuencias = [frecs_dict[s] for s in simbolos]

    raiz = construir_arbol(simbolos, frecuencias)

    print(Fore.CYAN + "\n🚀 Iniciando recorrido del árbol de Huffman para generar códigos...\n")
    codigos = recorrer_interactivo(raiz)

    mostrar_codigos(codigos, frecs_dict)

    print(Fore.CYAN + Style.BRIGHT + "\nGracias por usar el codificador de Huffman interactivo. ¡Hasta la próxima!\n")