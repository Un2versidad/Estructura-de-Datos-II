import networkx as nx
import matplotlib.pyplot as plt
import folium
import branca.colormap as cm

# Coordenadas de ciudades
ciudades = {
    'Panama': (8.9833, -79.5167),
    'Colon': (9.3592, -79.9014),
    'David': (8.4333, -82.4333),
    'Aguadulce': (8.2422, -80.5444),
    'Almirante': (9.2981, -82.4017),
    'Antón': (8.4000, -80.1667),
    'Bugaba': (8.4833, -82.6167),
    'Capira': (8.7500, -79.8667),
    'Chame': (8.5833, -79.8833),
    'Changuinola': (9.4306, -82.5158),
    'Chepo': (9.1667, -79.1000),
    'Chitré': (7.9667, -80.4333),
    'La Chorrera': (8.8803, -79.7833),
    'La Pintada': (8.6000, -80.4333),
    'La Villa de Los Santos': (7.9000, -80.3800),
    'Las Tablas': (7.7667, -80.2833),
    'Penonomé': (8.5167, -80.3500),
    'Puerto Armuelles': (8.2833, -82.8667),
    'Santiago': (8.1000, -80.9833),
    'Soná': (8.0167, -81.3167)
}

# Crear grafo
G = nx.Graph()
for ciudad, coord in ciudades.items():
    G.add_node(ciudad, pos=coord)

# Agregar rutas reales
G.add_edge('Panama', 'Colon', weight=80)
G.add_edge('Panama', 'La Chorrera', weight=35)
G.add_edge('La Chorrera', 'Capira', weight=20)
G.add_edge('Capira', 'Chame', weight=25)
G.add_edge('Chame', 'Penonomé', weight=60)
G.add_edge('Penonomé', 'Aguadulce', weight=30)
G.add_edge('Aguadulce', 'Antón', weight=15)
G.add_edge('Aguadulce', 'Santiago', weight=90)
G.add_edge('Santiago', 'Soná', weight=50)
G.add_edge('Santiago', 'Chitré', weight=70)
G.add_edge('Chitré', 'La Villa de Los Santos', weight=10)
G.add_edge('La Villa de Los Santos', 'Las Tablas', weight=30)
G.add_edge('David', 'Bugaba', weight=35)
G.add_edge('Bugaba', 'Puerto Armuelles', weight=60)
G.add_edge('David', 'Almirante', weight=120)
G.add_edge('Almirante', 'Changuinola', weight=20)
G.add_edge('Panama', 'Chepo', weight=50)
G.add_edge('David', 'Santiago', weight=170)

# VISUALIZACIÓN CON MATPLOTLIB
plt.figure(figsize=(15, 10))

# Obtener posiciones de nodos y ajustar
pos = nx.get_node_attributes(G, 'pos')
pos_plot = {city: (coord[1], coord[0]) for city, coord in pos.items()}

# Ajustar posiciones para la visualización (desplazamiento manual para ciudades superpuestas)
offset = 0.15  # Offset aumentado para hacer la separación más visible
pos_plot['Chitré'] = (pos_plot['Chitré'][0] - offset / 2, pos_plot['Chitré'][1] + offset / 2)
pos_plot['La Villa de Los Santos'] = (pos_plot['La Villa de Los Santos'][0] + offset / 2,
                                      pos_plot['La Villa de Los Santos'][1] - offset / 2)
# Agregar esta línea para corregir la superposición de Las Tablas
pos_plot['Las Tablas'] = (pos_plot['Las Tablas'][0] - offset / 2,
                          pos_plot['Las Tablas'][1] - offset / 2)
# Dibujar nodos
nx.draw_networkx_nodes(G, pos_plot, node_size=700, node_color='skyblue')

# Dibujar aristas
nx.draw_networkx_edges(G, pos_plot, width=2.0, edge_color='#444444')

# Dibujar etiquetas de nodos
nx.draw_networkx_labels(G, pos_plot, font_size=10, font_weight='bold')

# Dibujar etiquetas de aristas con pesos
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_plot, edge_labels=edge_labels,
                             font_color='red', font_size=9,
                             bbox=dict(facecolor='white', alpha=0.7))

plt.title('Grafo de rutas entre ciudades de Panamá', fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# VISUALIZACIÓN MEJORADA CON FOLIUM
# Crear el mapa centrado en Panamá
map_center = [8.5, -80.5]  # Centro aproximado de Panamá
m = folium.Map(location=map_center, zoom_start=8, tiles='CartoDB positron')

# Agregar un título atractivo
title_html = '''
<div style="position: fixed;
    top: 10px; left: 50px; width: 600px; height: 60px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px; padding: 10px; z-index: 9999;">
    <h3 style="color: #1A5276; text-align: center; margin: 0;">Rutas entre Ciudades de Panamá</h3>
    <p style="color: #566573; text-align: center; margin: 0;">Distancias en kilómetros</p>
</div>
'''
m.get_root().html.add_child(folium.Element(title_html))

# Crear un mapa de colores para ciudades basado en conectividad (grado de nodo)
degree_dict = dict(G.degree())
city_colors = {
    'capital': '#E74C3C',  # Rojo para Ciudad de Panamá (capital)
    'major': '#3498DB',    # Azul para ciudades principales
    'medium': '#2ECC71',   # Verde para ciudades medianas
    'minor': '#F39C12'     # Naranja para ciudades pequeñas
}

# Categorizar ciudades
major_cities = ['Panama', 'David', 'Colon', 'Santiago']
medium_cities = ['Chitré', 'Aguadulce', 'Penonomé', 'La Chorrera', 'Las Tablas']

# Agregar ciudades como marcadores con estilo atractivo
for city, coords in ciudades.items():
    # Determinar tipo de ciudad y color
    if city == 'Panama':
        color = city_colors['capital']
        radius = 12
        icon = 'star'
    elif city in major_cities:
        color = city_colors['major']
        radius = 10
        icon = 'info-sign'
    elif city in medium_cities:
        color = city_colors['medium']
        radius = 8
        icon = 'ok-sign'
    else:
        color = city_colors['minor']
        radius = 6
        icon = 'record'

    # Crear un popup con información de la ciudad
    popup_content = f"""
    <div style="width: 200px;">
        <h4 style="color: {color}; margin-bottom: 5px;">{city}</h4>
        <p><b>Coordenadas:</b> {coords[0]:.4f}, {coords[1]:.4f}</p>
        <p><b>Conexiones:</b> {degree_dict[city]}</p>
    </div>
    """

    # Agregar marcador
    folium.Marker(
        location=[coords[0], coords[1]],
        icon=folium.Icon(color=color.lstrip('#'), icon=icon, prefix='glyphicon'),
        tooltip=city
    ).add_to(m)

    # Agregar marcador circular para énfasis visual
    folium.CircleMarker(
        location=[coords[0], coords[1]],
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.4,
        weight=2,
        popup=folium.Popup(popup_content, max_width=300)
    ).add_to(m)

# Crear un mapa de colores para rutas basado en distancia
max_weight = max([data['weight'] for _, _, data in G.edges(data=True)])
min_weight = min([data['weight'] for _, _, data in G.edges(data=True)])
route_colormap = cm.LinearColormap(
    ['#1E88E5', '#FFC107', '#D81B60'],
    vmin=min_weight, vmax=max_weight,
    caption='Distancia (km)'
)
m.add_child(route_colormap)

# Agregar rutas como líneas con coloración gradiente basada en peso
for source, target, data in G.edges(data=True):
    source_coords = ciudades[source]
    target_coords = ciudades[target]
    weight = data['weight']

    # Escalar ancho de línea basado en importancia de la ruta (inverso del peso)
    line_width = 5 - (weight / max_weight * 3)  # Rango: 2-5
    if line_width < 2:
        line_width = 2

    # Obtener color basado en peso
    color = route_colormap(weight)

    # Crear línea con estilo atractivo
    folium.PolyLine(
        locations=[[source_coords[0], source_coords[1]],
                   [target_coords[0], target_coords[1]]],
        weight=line_width,
        color=color,
        opacity=0.8,
        tooltip=f"{source} → {target}: {weight} km",
        dash_array='5, 5' if weight > 100 else None,  # Patrón de línea discontinua para rutas largas
    ).add_to(m)

    # Agregar peso como una etiqueta elegante en el medio de la línea
    mid_point = [(source_coords[0] + target_coords[0]) / 2,
                 (source_coords[1] + target_coords[1]) / 2]

    folium.Marker(
        location=mid_point,
        icon=folium.DivIcon(
            icon_size=(50, 25),
            icon_anchor=(25, 12),
            html=f'''
            <div style="
                font-size: 10pt;
                font-weight: bold;
                color: #000;
                background-color: rgba(255, 255, 255, 0.8);
                border: 2px solid {color};
                border-radius: 10px;
                padding: 2px 5px;
                text-align: center;
                box-shadow: 0 0 5px rgba(0,0,0,0.2);">
                {weight} km
            </div>'''
        )
    ).add_to(m)

# Agregar una leyenda
legend_html = '''
<div style="position: fixed;
    bottom: 50px; right: 50px; width: 180px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px; padding: 10px; z-index: 9999;">
    <p style="margin-bottom: 5px;"><b>Ciudades</b></p>
    <p style="margin: 2px;"><i class="glyphicon glyphicon-star" style="color: #E74C3C;"></i> Capital</p>
    <p style="margin: 2px;"><i class="glyphicon glyphicon-info-sign" style="color: #3498DB;"></i> Ciudad principal</p>
    <p style="margin: 2px;"><i class="glyphicon glyphicon-ok-sign" style="color: #2ECC71;"></i> Ciudad mediana</p>
    <p style="margin: 2px;"><i class="glyphicon glyphicon-record" style="color: #F39C12;"></i> Ciudad pequeña</p>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Guardar en archivo HTML
m.save("panama_routes_map.html")

# Imprimir información del grafo
print("Información del grafo:")
print(f"• Nodos (ciudades): {G.number_of_nodes()}")
print(f"• Aristas (conexiones): {G.number_of_edges()}")
print(f"• Tipo: Grafo no dirigido (bidireccional) y ponderado (con pesos)")