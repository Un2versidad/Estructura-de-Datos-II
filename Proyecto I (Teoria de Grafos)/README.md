# Menu de Grafos - Ejemplo de uso

Este programa implementa un menú interactivo en consola para trabajar con grafos, permitiendo:

✅ Añadir vértices  
✅ Añadir arcos con pesos  
✅ Recorridos en anchura (BFS) y profundidad (DFS)  
✅ Búsqueda de vértices  
✅ Cálculo de distancia entre nodos (sumando pesos)  
✅ Visualización gráfica automática del grafo  

---

## Menú principal

El programa muestra el siguiente menú:

```
=== MENÚ DE OPERACIONES CON GRAFOS ===
1. Añadir vértice
2. Añadir arco
3. Recorrido en Anchura (BFS)
4. Recorrido en Profundidad (DFS)
5. Buscar vértice
6. Encontrar distancia entre dos nodos
7. Visualizar grafo
8. Salir
```

---

## Ejemplo de sesión completa

A continuación se muestra un **ejemplo de uso real** en consola:

---

### ✅ Añadir vértices

```
Seleccione una opción: 1

--- AÑADIR VÉRTICE ---
Ingrese el nombre del vértice: A
Vértice A añadido exitosamente.
```

```
Seleccione una opción: 1
Ingrese el nombre del vértice: B
Vértice B añadido exitosamente.
```

```
Seleccione una opción: 1
Ingrese el nombre del vértice: C
Vértice C añadido exitosamente.
```

```
Seleccione una opción: 1
Ingrese el nombre del vértice: D
Vértice D añadido exitosamente.
```

---

### ✅ Añadir arco con peso

```
Seleccione una opción: 2

--- AÑADIR ARCO ---
Ingrese el primer vértice: A
Ingrese el segundo vértice: B
Ingrese el peso del arco: 5.2
Arco entre A y B con peso 5.2 añadido.
```

---

### ✅ Recorrido en Anchura (BFS)

```
Seleccione una opción: 3

--- RECORRIDO EN ANCHURA (BFS) ---
Ingrese el nodo inicial para BFS: A
Recorrido BFS desde A: A -> B
```

---

### ✅ Recorrido en Profundidad (DFS)

```
Seleccione una opción: 4

--- RECORRIDO EN PROFUNDIDAD (DFS) ---
Ingrese el nodo inicial para DFS: A
Recorrido DFS desde A: A -> B
```

---

### ✅ Buscar vértice

```
Seleccione una opción: 5

--- BUSCAR VÉRTICE ---
Ingrese el vértice a buscar: B
El vértice B existe en el grafo.
```

---

### ✅ Encontrar distancia entre nodos

```
Seleccione una opción: 6

--- ENCONTRAR DISTANCIA ENTRE NODOS ---
Ingrese el nodo origen: B
Ingrese el nodo destino: A
La distancia entre B y A es: 5.2
Camino: B -> A
```

---

### ✅ Visualizar grafo

```
Seleccione una opción: 7

--- VISUALIZAR GRAFO ---
Se guardará la imagen en la carpeta 'graph_output' y se abrirá automáticamente.
Imagen guardada en: C:\Users\fl2on\PycharmProjects\PythonProject28\graph_output\graph_visualization.png
Abriendo visualización del grafo...
```

---

### ✅ Seguir añadiendo arcos y visualizar nuevamente

```
Seleccione una opción: 2
Ingrese el primer vértice: A
Ingrese el segundo vértice: D
Ingrese el peso del arco: 2.1
Arco entre A y D con peso 2.1 añadido.
```

```
Seleccione una opción: 2
Ingrese el primer vértice: B
Ingrese el segundo vértice: D
Ingrese el peso del arco: 4.5
Arco entre B y D con peso 4.5 añadido.
```

```
Seleccione una opción: 2
Ingrese el primer vértice: C
Ingrese el segundo vértice: D
Ingrese el peso del arco: 9.3
Arco entre C y D con peso 9.3 añadido.
```

```
Seleccione una opción: 7

--- VISUALIZAR GRAFO ---
Se guardará la imagen en la carpeta 'graph_output' y se abrirá automáticamente.
Imagen guardada en: C:\Users\fl2on\PycharmProjects\PythonProject28\graph_output\graph_visualization.png
Abriendo visualización del grafo...
```
---

## 📸 Ejemplo del Screenshot de Visualizacion

![graph_visualization](https://github.com/user-attachments/assets/d3a4023d-3d9c-475f-b062-952a2a010997)

## 📌 Notas

- Las rutas pueden variar dependiendo del sistema operativo.
- El grafo se guarda en la carpeta `graph_output`.
- Puedes repetir las opciones cuantas veces quieras para construir tu grafo.
