# DESARROLLE EL PROGRAMA QUE DETERMINA  EL RECORRIDO DE UN GRAFO, YA SEA EN ANCHURA O PROFUNDIDAD. UTILICE EL JAVA, C++, PHYTON U OTRO. ADJUNTE EL ARCHIVO

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def crear_grafo_ejemplo():
    G = nx.Graph()
    for i in range(1, 9):
        G.add_node(i)
    aristas = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
               (4, 8), (5, 8), (6, 8), (7, 8)]
    G.add_edges_from(aristas)
    return G

def crear_grafo_manual():
    G = nx.Graph()
    n = int(input("¿Cuántos nodos tendrá el grafo?: "))
    for i in range(1, n + 1):
        G.add_node(i)

    print("\nIngrese las aristas como pares de nodos (ej. 1 2). Escriba 'fin' para terminar.")
    while True:
        entrada = input("Arista (nodo1 nodo2): ")
        if entrada.lower() == 'fin':
            break
        try:
            u, v = map(int, entrada.split())
            if u in G.nodes() and v in G.nodes():
                G.add_edge(u, v)
            else:
                print("Uno de los nodos no existe. Intente de nuevo.")
        except:
            print("Entrada inválida. Use el formato: nodo1 nodo2")

    return G

def recorrido_anchura(G, inicio):
    visitados = []
    cola = deque([inicio])
    padre = {inicio: None}
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.append(nodo)
            for vecino in G.neighbors(nodo):
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
                    if vecino not in padre:
                        padre[vecino] = nodo
    return visitados, padre

def recorrido_profundidad(G, inicio):
    visitados = []
    padre = {inicio: None}
    def dfs(nodo):
        visitados.append(nodo)
        for vecino in G.neighbors(nodo):
            if vecino not in visitados:
                padre[vecino] = nodo
                dfs(vecino)
    dfs(inicio)
    return visitados, padre

def visualizar_recorrido(G, recorrido, padre, titulo):
    plt.figure(figsize=(10, 6))
    plt.title(titulo)
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    aristas_normales = [(u, v) for u, v in G.edges() if v != padre.get(u) and u != padre.get(v)]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_normales, width=1, alpha=0.5)
    aristas_recorrido = [(padre[nodo], nodo) for nodo in recorrido if padre[nodo] is not None]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_recorrido, width=2, edge_color='r')
    for i, nodo in enumerate(recorrido):
        plt.annotate(f"{i+1}", xy=pos[nodo], xytext=(10, 10), textcoords="offset points",
                     bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", alpha=0.8))
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def menu():
    G = None
    while True:
        print("\n=== RECORRIDO DE GRAFOS ===")
        print("1. Usar grafo de ejemplo")
        print("2. Ingresar grafo manualmente")
        print("3. Visualizar grafo")
        print("4. Recorrido en Anchura (BFS)")
        print("5. Recorrido en Profundidad (DFS)")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            G = crear_grafo_ejemplo()
            print("Grafo de ejemplo cargado.")

        elif opcion == "2":
            G = crear_grafo_manual()
            print("Grafo manual creado.")

        elif opcion == "3":
            if G is None:
                print("Primero debe cargar o crear un grafo.")
            else:
                plt.figure(figsize=(8, 6))
                plt.title("Grafo actual")
                nx.draw(G, with_labels=True, node_color='lightblue',
                        node_size=500, font_weight='bold')
                plt.axis('off')
                plt.show()

        elif opcion == "4":
            if G is None:
                print("Primero debe cargar o crear un grafo.")
                continue
            try:
                inicio = int(input("Ingrese el nodo inicial: "))
                if inicio not in G.nodes():
                    print(f"Error: El nodo {inicio} no existe en el grafo.")
                    continue
                recorrido, padre = recorrido_anchura(G, inicio)
                print(f"Recorrido en anchura desde {inicio}: {recorrido}")
                visualizar_recorrido(G, recorrido, padre, f"Recorrido en Anchura (BFS) desde nodo {inicio}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        elif opcion == "5":
            if G is None:
                print("Primero debe cargar o crear un grafo.")
                continue
            try:
                inicio = int(input("Ingrese el nodo inicial: "))
                if inicio not in G.nodes():
                    print(f"Error: El nodo {inicio} no existe en el grafo.")
                    continue
                recorrido, padre = recorrido_profundidad(G, inicio)
                print(f"Recorrido en profundidad desde {inicio}: {recorrido}")
                visualizar_recorrido(G, recorrido, padre, f"Recorrido en Profundidad (DFS) desde nodo {inicio}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

menu()