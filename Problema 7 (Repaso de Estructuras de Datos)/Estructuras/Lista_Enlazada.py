from colorama import Fore, Style
import tabulate

# Implementación de Lista Enlazada
class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, producto):
        nuevo_nodo = Nodo(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar(self, codigo):
        if not self.cabeza:
            return False

        if self.cabeza.producto.codigo == codigo:
            self.cabeza = self.cabeza.siguiente
            return True

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.producto.codigo != codigo:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            return True
        return False

    def buscar(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.producto.codigo == codigo:
                return actual.producto
            actual = actual.siguiente
        return None

    def buscar_por_nombre(self, nombre):
        resultados = []
        actual = self.cabeza
        while actual:
            if nombre.lower() in actual.producto.nombre.lower():
                resultados.append(actual.producto)
            actual = actual.siguiente
        return resultados

    def mostrar(self):
        actual = self.cabeza
        productos = []
        while actual:
            productos.append([actual.producto.nombre, actual.producto.codigo,
                              actual.producto.cantidad, f"${actual.producto.precio}"])
            actual = actual.siguiente

        if productos:
            print(tabulate(productos, headers=["Nombre", "Código", "Cantidad", "Precio"], tablefmt="grid"))
        else:
            print(Fore.YELLOW + "No hay productos en la lista" + Style.RESET_ALL)