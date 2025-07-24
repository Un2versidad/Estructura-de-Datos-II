import os
from time import sleep

# Lista Doblemente Enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual

    def obtener_top(self):
        if self.cabeza is None:
            return None
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual.valor

    def quitar_top(self):
        if self.cabeza is None:
            return None

        if self.cabeza.siguiente is None:
            valor = self.cabeza.valor
            self.cabeza = None
            return valor

        nodo_actual = self.cabeza
        while nodo_actual.siguiente.siguiente:
            nodo_actual = nodo_actual.siguiente

        valor = nodo_actual.siguiente.valor
        nodo_actual.siguiente = None
        return valor

    def esta_vacia(self):
        return self.cabeza is None

    def a_lista(self):
        resultado = []
        nodo_actual = self.cabeza
        while nodo_actual:
            resultado.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return resultado

class TorreHanoi:
    def __init__(self, num_discos):
        self.torres = [ListaDoblementeEnlazada() for _ in range(3)]
        self.num_discos = num_discos
        self.movimientos = 0
        self.juego_iniciado = False  # Variable para controlar si el juego ha comenzado

        # Inicializar la primera torre con los discos
        for disco in range(num_discos, 0, -1):
            self.torres[0].agregar(disco)

    def mostrar_torres(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Torre de Hanoi ===")
        print(f"Movimientos: {self.movimientos}\n")

        # Convertir torres a listas para facilitar la visualización
        torres_lista = [torre.a_lista() for torre in self.torres]
        max_altura = max(len(torre) for torre in torres_lista)

        # Mostrar torres
        for nivel in range(max_altura - 1, -1, -1):
            for torre in torres_lista:
                if nivel < len(torre):
                    disco = torre[nivel]
                    print(f"{'#' * disco:^7}", end="  ")
                else:
                    print(f"|{' ':^5}|", end="  ")
            print()

        # Mostrar base de las torres
        print("=" * 23)
        print("  A     B     C  ")
        print()

    def mover_disco(self, origen, destino):
        # Convertir letras a índices
        origen_idx = ord(origen.upper()) - ord('A')
        destino_idx = ord(destino.upper()) - ord('A')

        # Validar índices
        if not (0 <= origen_idx <= 2 and 0 <= destino_idx <= 2):
            print("¡Torres inválidas! Use A, B o C.")
            return False

        # Verificar si hay disco para mover
        if self.torres[origen_idx].esta_vacia():
            print("¡No hay discos en la torre de origen!")
            return False

        disco_mover = self.torres[origen_idx].obtener_top()

        # Verificar si el movimiento es válido
        if not self.torres[destino_idx].esta_vacia():
            disco_destino = self.torres[destino_idx].obtener_top()
            if disco_mover > disco_destino:
                print("¡Movimiento inválido! No puede colocar un disco más grande sobre uno más pequeño.")
                return False

        # Realizar el movimiento
        disco = self.torres[origen_idx].quitar_top()
        self.torres[destino_idx].agregar(disco)
        self.movimientos += 1
        self.juego_iniciado = True  # Marcar que el juego ha comenzado
        return True

    def verificar_victoria(self):
        # Si el juego no ha comenzado, no puede haber victoria
        if not self.juego_iniciado:
            return False

        # Revisar solo las torres B y C (índices 1 y 2) para la victoria
        for torre_idx in range(1, 3):  # Solo revisar torres B y C
            # Verificar si esta torre tiene todos los discos
            torre_actual = self.torres[torre_idx].a_lista()

            if len(torre_actual) == self.num_discos:
                # Verificar que las otras torres estén vacías
                otras_torres_vacias = all(
                    self.torres[i].esta_vacia() 
                    for i in range(3) 
                    if i != torre_idx
                )

                if not otras_torres_vacias:
                    continue

                # Verificar que los discos estén en orden correcto (mayor a menor)
                for i in range(len(torre_actual) - 1):
                    if torre_actual[i] <= torre_actual[i + 1]:
                        return False

                # Si llegamos aquí, encontramos una solución válida
                return True

        return False

def jugar_hanoi():
    while True:
        try:
            num_discos = int(input("Ingrese el número de discos (3-8): "))
            if 3 <= num_discos <= 8:
                break
            print("Por favor ingrese un número entre 3 y 8.")
        except ValueError:
            print("Por favor ingrese un número válido.")

    juego = TorreHanoi(num_discos)

    while not juego.verificar_victoria():
        juego.mostrar_torres()

        # Solicitar movimiento
        print("\nIngrese su movimiento (ejemplo: A C para mover de torre A a torre C)")
        print("O 'q' para salir")

        movimiento = input("Movimiento: ").strip().lower()
        if movimiento == 'q':
            print("\n¡Juego terminado!")
            break

        if len(movimiento) != 3 or movimiento[1] != ' ':
            print("Formato inválido. Use 'origen destino' (ejemplo: A C)")
            sleep(2)
            continue

        origen, destino = movimiento[0], movimiento[2]
        juego.mover_disco(origen, destino)

        if juego.verificar_victoria():
            juego.mostrar_torres()
            print(f"\n¡Felicitaciones! Has completado el juego en {juego.movimientos} movimientos!")
            print(f"Movimientos mínimos posibles: {2**num_discos - 1}")

if __name__ == "__main__":
    jugar_hanoi()
