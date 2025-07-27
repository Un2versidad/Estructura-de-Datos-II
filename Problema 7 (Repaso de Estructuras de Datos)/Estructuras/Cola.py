from colorama import Fore, Style
import tabulate

# Cola para pedidos de clientes
class ColaPedidos:
    def __init__(self):
        self.cola = []

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
        if not self.cola:
            return None
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar(self):
        if self.esta_vacia():
            print(Fore.YELLOW + "No hay pedidos en la cola" + Style.RESET_ALL)
            return

        pedidos = []
        for i, cliente in enumerate(self.cola):
            pedidos.append([i + 1, cliente.nombre, len(cliente.productos)])

        print(tabulate(pedidos, headers=["#", "Cliente", "Productos"], tablefmt="grid"))