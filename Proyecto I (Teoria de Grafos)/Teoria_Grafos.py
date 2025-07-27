import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import os
import subprocess
import platform

class GrafoMenu:
    def __init__(self):
        self.graph = nx.Graph()
        # Crear directorio para guardar la imagen si no existe
        os.makedirs("graph_output", exist_ok=True)
        self.output_path = os.path.join(os.getcwd(), "graph_output", "graph_visualization.png")

    def add_vertex(self, vertex):
        """Añade un vértice al grafo"""
        self.graph.add_node(vertex)
        print(f"Vértice {vertex} añadido exitosamente.")

    def add_edge(self, vertex1, vertex2, weight=1):
        """Añade un arco con peso entre dos vértices"""
        if not self.graph.has_node(vertex1):
            print(f"El vértice {vertex1} no existe.")
            return
        if not self.graph.has_node(vertex2):
            print(f"El vértice {vertex2} no existe.")
            return

        self.graph.add_edge(vertex1, vertex2, weight=weight)
        print(f"Arco entre {vertex1} y {vertex2} con peso {weight} añadido.")

    def visualize_graph(self):
        """Visualiza el grafo y guarda la imagen"""
        if not self.graph.nodes():
            print("El grafo está vacío.")
            return

        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(10, 7))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_weight='bold')

        # Dibujar los pesos de las aristas
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.title("Visualización del Grafo")

        # Guardar la imagen
        plt.savefig(self.output_path, bbox_inches='tight', dpi=300)
        plt.close()

        print(f"Imagen guardada en: {self.output_path}")

        # Abrir la imagen con el visor predeterminado
        self._open_file(self.output_path)

    def _open_file(self, filepath):
        """Abre un archivo con la aplicación predeterminada según el sistema operativo"""
        try:
            if platform.system() == 'Windows':
                os.startfile(filepath)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call(['open', filepath])
            else:  # Linux y otros
                subprocess.call(['xdg-open', filepath])
            print("Abriendo visualización del grafo...")
        except Exception as e:
            print(f"No se pudo abrir la imagen: {e}")
            print(f"Por favor, abra manualmente el archivo en: {filepath}")

    def bfs_traversal(self, start_vertex):
        """Recorrido en Anchura (BFS)"""
        if not self.graph.has_node(start_vertex):
            print(f"El vértice {start_vertex} no existe.")
            return []

        visited = set()
        queue = deque([start_vertex])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                queue.extend(neighbor for neighbor in self.graph.neighbors(vertex) if neighbor not in visited)

        return traversal

    def dfs_traversal(self, start_vertex):
        """Recorrido en Profundidad (DFS)"""
        if not self.graph.has_node(start_vertex):
            print(f"El vértice {start_vertex} no existe.")
            return []

        visited = set()
        stack = [start_vertex]
        traversal = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                stack.extend(
                    neighbor for neighbor in reversed(list(self.graph.neighbors(vertex))) if neighbor not in visited)

        return traversal

    def search_vertex(self, vertex):
        """Busca un vértice en el grafo"""
        return self.graph.has_node(vertex)

    def find_distance(self, source, target):
        """Encuentra la distancia entre dos nodos usando BFS"""
        if not self.graph.has_node(source):
            print(f"El vértice origen {source} no existe.")
            return -1
        if not self.graph.has_node(target):
            print(f"El vértice destino {target} no existe.")
            return -1
        if source == target:
            return 0

        # Usar algoritmo de Dijkstra para encontrar el camino más corto
        try:
            path = nx.dijkstra_path(self.graph, source, target, weight='weight')
            distance = 0

            # Calcular la distancia total sumando los pesos
            for i in range(len(path) - 1):
                distance += self.graph[path[i]][path[i + 1]]['weight']

            return distance, path
        except nx.NetworkXNoPath:
            print(f"No existe camino entre {source} y {target}.")
            return -1, []

def main():
    grafo_menu = GrafoMenu()

    while True:
        print("\n=== MENÚ DE OPERACIONES CON GRAFOS ===")
        print("1. Añadir vértice")
        print("2. Añadir arco")
        print("3. Recorrido en Anchura (BFS)")
        print("4. Recorrido en Profundidad (DFS)")
        print("5. Buscar vértice")
        print("6. Encontrar distancia entre dos nodos")
        print("7. Visualizar grafo")
        print("8. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            print("\n--- AÑADIR VÉRTICE ---")
            print("Ejemplos: A, B, 1, Madrid (ingrese un único valor)")
            vertex = input("Ingrese el nombre del vértice: ")
            grafo_menu.add_vertex(vertex)

        elif option == "2":
            print("\n--- AÑADIR ARCO ---")
            print("Primero ingrese un vértice origen (ej: A)")
            print("Luego ingrese un vértice destino (ej: B)")
            print("Finalmente ingrese un único valor numérico para el peso (ej: 5.2)")
            vertex1 = input("Ingrese el primer vértice: ")
            vertex2 = input("Ingrese el segundo vértice: ")
            try:
                weight = float(input("Ingrese el peso del arco: "))
                grafo_menu.add_edge(vertex1, vertex2, weight)
            except ValueError:
                print("Peso inválido. Ingrese un número.")

        elif option == "3":
            print("\n--- RECORRIDO EN ANCHURA (BFS) ---")
            print("Ingrese un único vértice existente (ej: A)")
            start = input("Ingrese el nodo inicial para BFS: ")
            result = grafo_menu.bfs_traversal(start)
            if result:
                print(f"Recorrido BFS desde {start}: {' -> '.join(map(str, result))}")

        elif option == "4":
            print("\n--- RECORRIDO EN PROFUNDIDAD (DFS) ---")
            print("Ingrese un único vértice existente (ej: A)")
            start = input("Ingrese el nodo inicial para DFS: ")
            result = grafo_menu.dfs_traversal(start)
            if result:
                print(f"Recorrido DFS desde {start}: {' -> '.join(map(str, result))}")

        elif option == "5":
            print("\n--- BUSCAR VÉRTICE ---")
            print("Ingrese un único vértice a buscar (ej: A)")
            vertex = input("Ingrese el vértice a buscar: ")
            found = grafo_menu.search_vertex(vertex)
            if found:
                print(f"El vértice {vertex} existe en el grafo.")
            else:
                print(f"El vértice {vertex} no existe en el grafo.")

        elif option == "6":
            print("\n--- ENCONTRAR DISTANCIA ENTRE NODOS ---")
            print("Ingrese un vértice origen (ej: A)")
            print("Ingrese un vértice destino (ej: B)")
            source = input("Ingrese el nodo origen: ")
            target = input("Ingrese el nodo destino: ")
            result = grafo_menu.find_distance(source, target)

            if isinstance(result, tuple) and result[0] >= 0:
                distance, path = result
                print(f"La distancia entre {source} y {target} es: {distance}")
                print(f"Camino: {' -> '.join(map(str, path))}")

        elif option == "7":
            print("\n--- VISUALIZAR GRAFO ---")
            print("Se guardará la imagen en la carpeta 'graph_output' y se abrirá automáticamente.")
            grafo_menu.visualize_graph()

        elif option == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
