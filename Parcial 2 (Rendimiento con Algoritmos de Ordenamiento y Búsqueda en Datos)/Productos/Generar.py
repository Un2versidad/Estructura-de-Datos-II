import random
from faker import Faker
from typing import List

# Inicializar Faker para generar datos realistas
fake = Faker('es_ES')

# Parte 1: Modelado de Datos
class Producto:
    """Clase que representa un producto en la tienda online."""

    def __init__(self, id: int, nombre: str, precio: float, categoria: str, stock: int, calificacion_promedio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacion_promedio = calificacion_promedio

    def __str__(self):
        return (f"Producto(id={self.id}, nombre='{self.nombre}', "
                f"precio=${self.precio:.2f}, categoría='{self.categoria}', "
                f"stock={self.stock}, calificación={self.calificacion_promedio:.1f})")

# Generación de datos de prueba
def generar_productos(cantidad: int) -> List[Producto]:
    """Genera una lista de productos aleatorios."""
    categorias = ["Electrónica", "Ropa", "Libros", "Hogar", "Deportes"]

    tipos_producto = {
        "Electrónica": ["Laptop", "Smartphone", "Auriculares", "Tablet", "Cámara", "Smartwatch", "Monitor"],
        "Ropa": ["Camisa", "Pantalón", "Vestido", "Chaqueta", "Zapatos", "Sudadera", "Abrigo"],
        "Libros": ["Novela", "Texto Académico", "Biografía", "Libro de Cocina", "Revista", "Cómic"],
        "Hogar": ["Silla", "Mesa", "Lámpara", "Sofá", "Cama", "Estantería", "Alfombra"],
        "Deportes": ["Balón", "Raqueta", "Zapatillas", "Bicicleta", "Mancuernas", "Camiseta"]
    }

    marcas = {
        "Electrónica": ["Samsung", "Apple", "Xiaomi", "Huawei", "Sony", "LG", "Lenovo"],
        "Ropa": ["Zara", "H&M", "Nike", "Adidas", "Mango", "Levis", "Puma"],
        "Libros": ["Anagrama", "Planeta", "Alfaguara", "Penguin", "Salamandra"],
        "Hogar": ["Ikea", "El Corte Inglés", "Conforama", "Maisons du Monde"],
        "Deportes": ["Nike", "Adidas", "Decathlon", "Puma", "Under Armour"]
    }

    productos = []
    for i in range(1, cantidad + 1):
        categoria = random.choice(categorias)
        tipo_producto = random.choice(tipos_producto[categoria])
        marca = random.choice(marcas[categoria])

        # Generamos nombres
        if random.random() < 0.7:  # 70% de probabilidad de usar marca
            nombre = f"{marca} {tipo_producto} {fake.word().capitalize()}"
        else:
            nombre = f"{tipo_producto} {fake.word().capitalize()} {fake.word().capitalize()}"

        # Rangos de precios según categoría
        if categoria == "Electrónica":
            precio = round(random.uniform(150.0, 1500.0), 2)
        elif categoria == "Ropa":
            precio = round(random.uniform(15.0, 150.0), 2)
        elif categoria == "Libros":
            precio = round(random.uniform(8.0, 50.0), 2)
        elif categoria == "Hogar":
            precio = round(random.uniform(30.0, 500.0), 2)
        else:  # Deportes
            precio = round(random.uniform(20.0, 300.0), 2)

        stock = random.randint(0, 100)

        # Distribución sesgada hacia calificaciones altas
        calificacion_base = random.uniform(2.5, 5.0)
        calificacion_promedio = round(min(5.0, calificacion_base), 1)

        productos.append(Producto(i, nombre, precio, categoria, stock, calificacion_promedio))

    return productos