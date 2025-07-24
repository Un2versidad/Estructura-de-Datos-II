![image](https://github.com/user-attachments/assets/a3d79bfd-db41-439e-a398-d3d0b4e5e6cd)

# 🎮 **Estructuras de Datos II - UIP** 🧠

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/Un2versidad/Estructura-de-Datos-II/blob/main/LICENSE)


## 📑 **Índice**

1. [Descripción del Problema](#-descripción-del-problema)
2. [Reglas del Juego](#-reglas-del-juego)
3. [Implementación con Lista Doblemente Enlazada](#-implementación-con-lista-doblemente-enlazada)
4. [Representación Gráfica de la Torre de Hanoi](#-representación-gráfica-de-la-torre-de-hanoi)
5. [Cómo Jugar](#-cómo-jugar)

## 🤔 **Descripción del Problema**

El **Problema de las Torres de Hanoi** 🏰 es un clásico rompecabezas matemático que consiste en mover una serie de discos de una varilla a otra, siguiendo ciertas reglas. Este problema es ampliamente utilizado para enseñar recursividad y estructuras de datos.

En este proyecto, implementamos la solución utilizando una **Lista Doblemente Enlazada** ↔️ para representar las torres y los discos.

## 📜 **Reglas del Juego**

El juego sigue estas tres simples reglas:

1. **Sólo se puede mover un disco cada vez** 🔄.
2. **Un disco de mayor tamaño no puede descansar sobre uno más pequeño** ⬆️⬇️.
3. **Sólo puedes desplazar el disco que se encuentre arriba en cada varilla** 🔝.

## 🔗 **Implementación con Lista Doblemente Enlazada**

### Descripción:
Utilizamos una **lista doblemente enlazada** ↔️ para representar las torres y los discos. Cada torre es una lista doblemente enlazada donde los discos se apilan como nodos.

### Funcionamiento:
- **Agregar un disco**: Se añade al final de la lista.
- **Quitar un disco**: Se elimina el último nodo (top de la torre).
- **Mover un disco**: Se quita de una torre y se agrega a otra, siempre validando las reglas del juego.

### Representación Gráfica de la Lista Doblemente Enlazada:

```
TORRE A
   |
   v
+-----+     +-----+     +-----+
|  3  |<--->|  2  |<--->|  1  |---> NULL
+-----+     +-----+     +-----+
```

> **Nota:** Cada número representa un disco, y las flechas indican las referencias entre nodos en ambas direcciones ↔️.

---

## 🏰 **Representación Gráfica de la Torre de Hanoi**

Aquí tienes una representación visual en ASCII art de cómo se verían las torres con 3 discos:

```
=== Torre de Hanoi ===

Movimientos: 0

    ###      |          |          |
   #####     |          |          |
  #######    |          |          |
======================================
     A             B           C  

```

> **Nota:** Los discos están representados por `#`, y las torres vacías por `|`. La base de las torres está representada por `=`.

## 🎮 **Cómo Jugar**

1. **Iniciar el Juego**:
   - Elige el número de discos (entre 3 y 8) al iniciar el programa.
   - Los discos se colocarán inicialmente en la **Torre A**.

2. **Realizar Movimientos**:
   - Ingresa el movimiento en el formato `origen destino` (ejemplo: `A C` para mover un disco de la Torre A a la Torre C).
   - Si deseas salir del juego, escribe `q`.

3. **Ganar el Juego**:
   - Mueve todos los discos a la **Torre B** o **Torre C** siguiendo las reglas.
   - ¡Felicitaciones si logras completar el juego en el número mínimo de movimientos! 🎉
