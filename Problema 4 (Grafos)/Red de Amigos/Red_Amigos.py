import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un grafo para la red de amigos
# En una red social, los nodos son los usuarios y las aristas son las conexiones de amistad
G = nx.Graph()  # Grafo no dirigido (las amistades son recíprocas)
# Si quisiéramos modelar seguidores (como en Twitter), usaríamos: G = nx.DiGraph()

# Agregar algunos usuarios (nodos) a la red
usuarios = [
    "Carlos", "María", "Juan", "Ana", "Pedro", "Lucía",
    "Miguel", "Sofía", "José", "Laura", "Diego", "Elena"
]

# Agregar nodos al grafo
G.add_nodes_from(usuarios)

# Crear algunas conexiones de amistad (aristas)
# Cada conexión puede tener un peso que representa la fuerza de la amistad
# (número de interacciones, tiempo de amistad, etc.)
amistades = [
    ("Carlos", "María", 8),
    ("Carlos", "Juan", 5),
    ("María", "Ana", 10),
    ("María", "Pedro", 3),
    ("Juan", "Pedro", 7),
    ("Juan", "Lucía", 2),
    ("Ana", "Lucía", 9),
    ("Pedro", "Miguel", 6),
    ("Lucía", "Sofía", 8),
    ("Miguel", "José", 4),
    ("Sofía", "Laura", 7),
    ("José", "Diego", 9),
    ("Laura", "Elena", 5),
    ("Diego", "Elena", 8),
    ("Elena", "Carlos", 3),
    ("Miguel", "Sofía", 10),
    ("Ana", "José", 2),
]

# Agregar aristas con pesos al grafo
for origen, destino, peso in amistades:
    G.add_edge(origen, destino, weight=peso)

# Calcular métricas de la red para visualización
# Centralidad de grado: número de conexiones que tiene cada usuario
centralidad_grado = dict(G.degree())

# Calcular comunidades utilizando el algoritmo de Louvain
try:
    from community import community_louvain
    particion = community_louvain.best_partition(G)
    colores_comunidad = [particion[nodo] for nodo in G.nodes()]
except ImportError:
    # Si no está instalado python-louvain, usar colores aleatorios
    colores_comunidad = [random.randint(0, 4) for _ in G.nodes()]

# Configurar la visualización
plt.figure(figsize=(12, 8))
plt.title("Red de Amigos en una Red Social", fontsize=16)

# Obtener una disposición de nodos que se vea bien
# Usamos spring_layout para simular un sistema de fuerzas físicas
pos = nx.spring_layout(G, k=0.5, seed=42)

# Dibujar nodos con tamaño basado en la centralidad de grado
# (usuarios con más amigos tienen nodos más grandes)
tamaños_nodos = [centralidad_grado[nodo] * 100 for nodo in G.nodes()]
nx.draw_networkx_nodes(G, pos,
                      node_size=tamaños_nodos,
                      node_color=colores_comunidad,
                      alpha=0.8,
                      cmap=plt.cm.rainbow)

# Obtener pesos de las aristas para la visualización
pesos = [G[u][v]['weight'] for u, v in G.edges()]
anchura_max = 5
anchura_min = 0.5
# Normalizar los pesos para el grosor de las líneas
anchuras = [anchura_min + (anchura_max - anchura_min) * peso / max(pesos) for peso in pesos]

# Dibujar aristas con grosor basado en el peso (fuerza de la amistad)
nx.draw_networkx_edges(G, pos,
                      width=anchuras,
                      alpha=0.5,
                      edge_color='gray')

# Dibujar etiquetas de los nodos (nombres de los usuarios)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Mostrar explícitamente los pesos de las aristas como etiquetas numéricas
edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             font_size=9,
                             font_color='red',
                             bbox=dict(facecolor='white', alpha=0.7))

# Agregar información sobre el grafo
plt.text(0.02, 0.02,
         f"Usuarios: {G.number_of_nodes()}\n"
         f"Conexiones: {G.number_of_edges()}\n"
         f"Tipo: Grafo no dirigido y ponderado",
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.8))

# Mostrar leyenda explicativa
plt.figtext(0.02, 0.95, "Características del Grafo:", fontsize=12, fontweight='bold')
plt.figtext(0.02, 0.92, "• Nodos: Representan usuarios de la red social", fontsize=10)
plt.figtext(0.02, 0.89, "• Aristas: Representan conexiones de amistad entre usuarios", fontsize=10)
plt.figtext(0.02, 0.86, "• Tamaño de nodo: Basado en número de amigos", fontsize=10)
plt.figtext(0.02, 0.83, "• Grosor de arista: Basado en la fuerza de la amistad", fontsize=10)
plt.figtext(0.02, 0.80, "• Número en arista: Valor exacto de la fuerza de amistad (1-10)", fontsize=10)
plt.figtext(0.02, 0.77, "• Color de nodo: Representa comunidades de usuarios", fontsize=10)

plt.axis('off')
plt.tight_layout()
plt.show()

# Imprimir estadísticas de la red
print("Estadísticas de la Red de Amigos:")
print(f"• Número de usuarios: {G.number_of_nodes()}")
print(f"• Número de conexiones de amistad: {G.number_of_edges()}")
print(f"• Densidad de la red: {nx.density(G):.4f}")
print(f"• Diámetro de la red: {nx.diameter(G)}")
print(f"• Usuario con más conexiones: {max(centralidad_grado.items(), key=lambda x: x[1])[0]}")
print(f"• Escala de ponderación: 1-10 (donde 10 es la amistad más fuerte)")