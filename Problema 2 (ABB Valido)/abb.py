# Problema 14: Verificar si un arbol binario de búsqueda es válido
# Clase que representa un nodo en un árbol binario
class NodoArbol:
    def __init__(self, valor=0, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

# Verifica si un árbol binario es un Árbol Binario de Búsqueda (ABB) válido
def es_abb_valido(nodo, valor_min=float('-inf'), valor_max=float('inf')):
    if not nodo:
        return True
    if nodo.valor <= valor_min or nodo.valor >= valor_max:
        return False
    return (es_abb_valido(nodo.izquierda, valor_min, nodo.valor) and
            es_abb_valido(nodo.derecha, nodo.valor, valor_max))

# Función auxiliar para mostrar resultados de forma ordenada
def mostrar_arbol(titulo, arbol_ascii, raiz):
    print("=" * 50)
    print(titulo)
    print(arbol_ascii)
    print("¿Es un ABB válido?:", es_abb_valido(raiz))
    print("=" * 50 + "\n")

# Ejemplo 1: Árbol válido
raiz1 = NodoArbol(5)
raiz1.izquierda = NodoArbol(3)
raiz1.derecha = NodoArbol(7)
raiz1.izquierda.izquierda = NodoArbol(2)
raiz1.izquierda.derecha = NodoArbol(4)
raiz1.derecha.derecha = NodoArbol(8)

arbol1 = """
     5
    / \\
   3   7
  / \\   \\
 2   4   8
"""

mostrar_arbol("Ejemplo 1: Árbol Binario de Búsqueda VÁLIDO", arbol1, raiz1)

# Ejemplo 2: Árbol inválido
raiz2 = NodoArbol(5)
raiz2.izquierda = NodoArbol(3)
raiz2.derecha = NodoArbol(3)

arbol2 = """
     5
    / \\
   3   3  <- Valor inválido (debería ser > 5)
"""

mostrar_arbol("Ejemplo 2: Árbol Binario de Búsqueda INVÁLIDO", arbol2, raiz2)