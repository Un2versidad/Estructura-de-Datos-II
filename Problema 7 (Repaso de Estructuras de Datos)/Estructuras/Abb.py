# Árbol Binario de Búsqueda
class NodoArbol:
    def __init__(self, producto):
        self.producto = producto
        self.izquierda = None
        self.derecha = None

class ABB:
    def __init__(self, tipo_clave='codigo'):
        self.raiz = None
        self.tipo_clave = tipo_clave

    def obtener_clave(self, producto):
        return producto.codigo if self.tipo_clave == 'codigo' else producto.nombre

    def insertar(self, producto):
        if not self.raiz:
            self.raiz = NodoArbol(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, nodo, producto):
        clave = self.obtener_clave(producto)
        clave_actual = self.obtener_clave(nodo.producto)

        if clave < clave_actual:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(producto)
            else:
                self._insertar_recursivo(nodo.izquierda, producto)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(producto)
            else:
                self._insertar_recursivo(nodo.derecha, producto)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None

        clave_actual = self.obtener_clave(nodo.producto)

        if clave == clave_actual:
            return nodo.producto
        if clave < clave_actual:
            return self._buscar_recursivo(nodo.izquierda, clave)
        return self._buscar_recursivo(nodo.derecha, clave)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.producto)
            self._inorden_recursivo(nodo.derecha, resultado)