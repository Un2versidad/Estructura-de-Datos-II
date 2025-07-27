import matplotlib.pyplot as plt
import networkx as nx
import os
import matplotlib.patches as mpatches

# Copyright © 2024 Franklin Leon. All rights reserved.

# Definir las matrices de adyacencia
matrices = {
    "a": [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ],
    "b": [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ],
    "c": [
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
}

# Descripciones para cada grafo
descripciones = {
    "a": "• Estructura tipo estrella (no pura)\n• Nodo 0 conectado a todos los demás\n• Conexión adicional entre nodos 1 y 2\n• Total: 4 nodos, 4 aristas",
    "b": "• Estructura cíclica\n• Cada nodo tiene exactamente 2 conexiones\n• Total: 4 nodos, 4 aristas",
    "c": "• Nodos centrales: 2 y 3 ambos con 3 conexiones\n• Nodos 0 y 1 con 2 conexiones cada uno\n• Total: 4 nodos, 5 aristas"
}

# Configurar figura para los grafos
fig, axes = plt.subplots(1, 3, figsize=(18, 8))
fig.suptitle('Representación de Grafos según Matrices de Adyacencia', fontsize=16, y=0.98)

# Añadir explicación general
fig.text(0.5, 0.02,
         'Un "1" en la posición (i,j) de la matriz indica que existe una conexión entre los nodos i y j.\nUn "0" indica que no hay conexión directa entre esos nodos.',
         ha='center', fontsize=11, bbox=dict(facecolor='lightyellow', alpha=0.5))

# Añadir copyright
fig.text(0.95, 0.01, '© Franklin Leon', ha='right', fontsize=8, color='gray')

# Colores para diferenciar cada grafo
node_colors = ['lightcoral', 'lightgreen', 'skyblue']
edge_colors = ['darkred', 'darkgreen', 'navy']

for i, (key, matrix) in enumerate(matrices.items()):
    G = nx.Graph()
    n = len(matrix)
    G.add_nodes_from(range(n))

    # Añadir aristas desde la matriz de adyacencia
    for u in range(n):
        for v in range(u + 1, n):
            if matrix[u][v]:
                G.add_edge(u, v)

    # Calcular grados de los nodos
    node_degrees = dict(G.degree())

    # Posicionar nodos
    pos = nx.spring_layout(G, seed=42)

    # Dibujar grafo
    nx.draw(G, pos, with_labels=True, ax=axes[i],
            node_color=node_colors[i],
            edge_color=edge_colors[i],
            node_size=700,
            font_weight='bold',
            width=2.5,
            font_size=12)

    # Mostrar matriz de adyacencia en texto
    matrix_text = "Matriz de adyacencia:\n"
    for row in matrix:
        matrix_text += str(row) + "\n"

    axes[i].text(0.5, -0.15, matrix_text, ha='center',
                 transform=axes[i].transAxes,
                 fontsize=9, family='monospace',
                 bbox=dict(facecolor='white', alpha=0.7))

    # Mostrar descripción
    axes[i].text(0.5, -0.35, descripciones[key], ha='center',
                 transform=axes[i].transAxes, fontsize=10,
                 bbox=dict(facecolor='white', alpha=0.7))

    # Añadir información del grado junto a cada nodo
    for node, (x, y) in pos.items():
        axes[i].annotate(f"Grado: {node_degrees[node]}",
                         xy=(x, y), xytext=(15, 10),
                         textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.7),
                         fontsize=8)

    axes[i].set_title(f"Grafo {key.upper()}", fontsize=14)
    axes[i].axis('off')

plt.tight_layout(rect=[0, 0.08, 1, 0.95])

# Guardar la imagen
image_output_path = "Grafos_a_b_c_explicados.png"
try:
    plt.savefig(image_output_path, dpi=300, bbox_inches='tight')
    print(f"Imagen guardada en: {os.path.abspath(image_output_path)}")
except Exception as e:
    print(f"Error al guardar la imagen: {e}")

plt.show()