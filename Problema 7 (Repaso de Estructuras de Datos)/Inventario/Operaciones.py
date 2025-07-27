from colorama import Fore, Style
from Estructuras.Abb import ABB
from Estructuras.Cola import ColaPedidos
from Estructuras.Lista_Enlazada import ListaEnlazada
from Estructuras.Pila import PilaOperaciones

class Cliente:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos  # Lista de tuplas (código, cantidad)

    def __str__(self):
        return f"Cliente: {self.nombre}, Productos: {len(self.productos)}"

class GestorInventario:
    def __init__(self):
        self.productos = []  # Implementación con array
        self.lista_enlazada = ListaEnlazada()
        self.operaciones = PilaOperaciones()
        self.pedidos = ColaPedidos()
        self.arbol_productos = ABB()

    def agregar_productos_iniciales(self, productos):
        for producto in productos:
            self.productos.append(producto)
            self.lista_enlazada.agregar(producto)
            self.arbol_productos.insertar(producto)

    def ordenar_por_nombre(self):
        self.productos.sort(key=lambda x: x.nombre)
        return self.productos

    def ordenar_por_precio(self):
        self.productos.sort(key=lambda x: x.precio)
        return self.productos

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.lista_enlazada.agregar(producto)
        self.arbol_productos.insertar(producto)
        self.operaciones.apilar(f"Agregado: {producto.nombre}")

    def eliminar_producto(self, codigo):
        producto = self.lista_enlazada.buscar(codigo)
        if producto:
            self.productos = [p for p in self.productos if p.codigo != codigo]
            self.lista_enlazada.eliminar(codigo)
            # Reconstruir árbol
            self.arbol_productos = ABB()
            for p in self.productos:
                self.arbol_productos.insertar(p)
            self.operaciones.apilar(f"Eliminado: {producto.nombre}")
            return True
        return False

    def editar_producto(self, codigo, nuevos_datos):
        producto = self.lista_enlazada.buscar(codigo)
        if producto:
            info_antigua = str(producto)
            for clave, valor in nuevos_datos.items():
                setattr(producto, clave, valor)
            self.operaciones.apilar(f"Editado: {info_antigua} → {producto}")
            return True
        return False

    def deshacer_ultima_operacion(self):
        operacion = self.operaciones.desapilar()
        if operacion:
            print(Fore.CYAN + f"Deshaciendo: {operacion}" + Style.RESET_ALL)
            return True
        return False

    def agregar_pedido_cliente(self, cliente):
        self.pedidos.encolar(cliente)
        print(Fore.GREEN + f"Pedido agregado para: {cliente.nombre}" + Style.RESET_ALL)

    def procesar_siguiente_pedido(self):
        if self.pedidos.esta_vacia():
            print(Fore.YELLOW + "No hay pedidos para procesar" + Style.RESET_ALL)
            return False

        cliente = self.pedidos.desencolar()
        print(Fore.CYAN + f"Procesando pedido para: {cliente.nombre}" + Style.RESET_ALL)

        for codigo, cantidad in cliente.productos:
            producto = self.lista_enlazada.buscar(codigo)
            if producto and producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                print(
                    Fore.GREEN + f"Completado: {cantidad} x {producto.nombre} (Quedan: {producto.cantidad})" + Style.RESET_ALL)
            else:
                if producto:
                    print(
                        Fore.RED + f"Stock insuficiente para {producto.nombre} - Código: {codigo}. Disponible: {producto.cantidad}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Producto no encontrado con código: {codigo}" + Style.RESET_ALL)
        return True