from tabulate import tabulate
from colorama import Fore, Style

# Pila para historial de operaciones
class PilaOperaciones:
    def __init__(self, tamano_max=10):
        self.pila = []
        self.tamano_max = tamano_max

    def apilar(self, operacion):
        if len(self.pila) >= self.tamano_max:
            self.pila.pop(0)
        self.pila.append(operacion)

    def desapilar(self):
        if not self.pila:
            return None
        return self.pila.pop()

    def mostrar(self):
        if not self.pila:
            print(Fore.YELLOW + "No hay operaciones en el historial" + Style.RESET_ALL)
            return

        operaciones = []
        for i, op in enumerate(reversed(self.pila)):
            operaciones.append([i + 1, op])

        print(tabulate(operaciones, headers=["#", "Operación"], tablefmt="grid"))