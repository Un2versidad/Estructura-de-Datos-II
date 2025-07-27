import random
from tabulate import tabulate
from colorama import Fore, init
from typing import List, Any
import time
from Productos.Busqueda import SistemaBusqueda, busqueda_lineal_por_nombre
from Productos.Generar import generar_productos
from Productos.Ordenamiento import ordenamiento_mezcla, ordenamiento_rapido, ordenamiento_insercion, medir_tiempo_ordenamiento
from Utilidades.Exportar_Datos import generar_pdf_productos
from Utilidades.Generar_Graficas import visualizar_rendimiento_ordenamiento, visualizar_comparacion_metodos_busqueda, visualizar_rendimiento_busqueda

# Inicializar colorama para salida con colores
init(autoreset=True)

# Función para generar tablas bonitas
def generar_tabla(datos: List[List[Any]], encabezados: List[str]) -> str:
    """Genera una tabla formateada con tabulate."""
    return tabulate(datos, headers=encabezados, tablefmt="grid")

def main():
    print(f"{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}{'SISTEMA DE GESTIÓN DE PRODUCTOS DE TIENDA EN LÍNEA':^60}")
    print(f"{Fore.CYAN}{'=' * 60}")

    # Generar productos (aumentado para mejor visualización de diferencias)
    num_productos = 1000  # Aumentado de 50 a 1000 para mejor medición*
    print(f"\n{Fore.YELLOW}Generando {num_productos} productos aleatorios...")
    productos = generar_productos(num_productos)
    print(f"{Fore.GREEN}✓ Productos generados exitosamente ({len(productos)} productos)")

    # Mostrar productos de ejemplo
    print(f"\n{Fore.YELLOW}Muestra de 50 productos generados (de {len(productos)} totales):")
    muestra_productos = productos[:50]  # Mostrar 50 productos de ejemplo
    datos_muestra = [[p.id, p.nombre, f"${p.precio:.2f}", p.categoria, p.stock, p.calificacion_promedio]
                     for p in muestra_productos]
    print(generar_tabla(datos_muestra,["ID", "Nombre", "Precio", "Categoría", "Stock", "Calificación"]))

    # Parte 2: Rendimiento de Ordenamiento
    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}{'ALGORITMOS DE ORDENAMIENTO':^60}")
    print(f"{Fore.CYAN}{'=' * 60}")

    # Definir criterios de ordenamiento
    clave_precio = lambda p: p.precio
    clave_calificacion = lambda p: p.calificacion_promedio

    # Inicializar lista de resultados para visualización combinada
    resultados_ordenamiento = []

    # Ordenar por precio (ascendente)
    print(f"\n{Fore.YELLOW}Ordenando por precio (ascendente):")
    resultados_precio = []

    for nombre_algoritmo, func_ordenamiento in [
        ("Merge Sort", ordenamiento_mezcla),
        ("Quick Sort", ordenamiento_rapido),
        ("Insertion Sort", ordenamiento_insercion)
    ]:
        tiempo, productos_ordenados = medir_tiempo_ordenamiento(func_ordenamiento, productos, clave_precio, False, 5)
        print(f"{Fore.WHITE}{nombre_algoritmo}: {Fore.GREEN}{tiempo:.3f} ms")

        # Mostrar ejemplo de productos ordenados
        if nombre_algoritmo == "Merge Sort":
            print(f"\n{Fore.YELLOW}Ejemplo de productos ordenados por precio (ascendente):")
            muestra_ordenada = productos_ordenados[:5]
            datos_muestra = [[p.id, p.nombre, f"${p.precio:.2f}", p.categoria]
                             for p in muestra_ordenada]
            print(generar_tabla(datos_muestra, ["ID", "Nombre", "Precio", "Categoría"]))

        resultado = {"algoritmo": nombre_algoritmo, "tiempo_ms": tiempo}
        resultados_precio.append(resultado)

        # Agregar a resultados combinados
        resultados_ordenamiento.append({
            'algoritmo': nombre_algoritmo,
            'criterio': 'Precio (asc)',
            'tiempo_ms': tiempo
        })

    # Ordenar por calificación (descendente)
    print(f"\n{Fore.YELLOW}Ordenando por calificación (descendente):")
    resultados_calificacion = []

    for nombre_algoritmo, func_ordenamiento in [
        ("Merge Sort", ordenamiento_mezcla),
        ("Quick Sort", ordenamiento_rapido),
        ("Insertion Sort", ordenamiento_insercion)
    ]:
        tiempo, productos_ordenados = medir_tiempo_ordenamiento(func_ordenamiento, productos, clave_calificacion, True,
                                                                5)
        print(f"{Fore.WHITE}{nombre_algoritmo}: {Fore.GREEN}{tiempo:.3f} ms")

        # Mostrar ejemplo de productos ordenados
        if nombre_algoritmo == "Merge Sort":
            print(f"\n{Fore.YELLOW}Ejemplo de productos ordenados por calificación (descendente):")
            muestra_ordenada = productos_ordenados[:5]
            datos_muestra = [[p.id, p.nombre, p.calificacion_promedio, p.categoria]
                             for p in muestra_ordenada]
            print(generar_tabla(datos_muestra, ["ID", "Nombre", "Calificación", "Categoría"]))

        resultado = {"algoritmo": nombre_algoritmo, "tiempo_ms": tiempo}
        resultados_calificacion.append(resultado)

        # Agregar a resultados combinados
        resultados_ordenamiento.append({
            'algoritmo': nombre_algoritmo,
            'criterio': 'Calificación (desc)',
            'tiempo_ms': tiempo
        })

    # Mostrar tabla de resultados
    print(f"\n{Fore.YELLOW}Resumen de Rendimiento de Ordenamiento:")
    tabla_datos = []
    for resultado in resultados_ordenamiento:
        tabla_datos.append([
            resultado['algoritmo'],
            resultado['criterio'],
            f"{resultado['tiempo_ms']:.3f} ms"
        ])

    print(generar_tabla(tabla_datos, ["Algoritmo", "Criterio", "Tiempo (ms)"]))

    # Visualizar rendimiento de ordenamiento combinado
    visualizar_rendimiento_ordenamiento(
        resultados_ordenamiento,
        "Comparación de Algoritmos de Ordenamiento",
        "rendimiento_ordenamiento.png"
    )

    # Parte 3: Rendimiento de Búsqueda
    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}{'ALGORITMOS DE BÚSQUEDA':^60}")
    print(f"{Fore.CYAN}{'=' * 60}")

    # Inicializar sistema de búsqueda
    sistema_busqueda = SistemaBusqueda(productos)
    sistema_busqueda.preparar_indices()

    # Búsqueda binaria de productos por ID
    print(f"\n{Fore.YELLOW}Búsqueda Binaria por ID:")

    # Buscar IDs existentes
    ids_existentes = random.sample([p.id for p in productos], 10)
    tiempos = []
    encontrados_existentes = 0

    for _ in range(20):  # Repetir para obtener mediciones más precisas
        inicio_tiempo = time.perf_counter()
        encontrados = 0
        for id in ids_existentes:
            producto = sistema_busqueda.buscar_por_id(id)
            if producto:
                encontrados += 1
        fin_tiempo = time.perf_counter()
        tiempos.append((fin_tiempo - inicio_tiempo) * 1000)
        encontrados_existentes = encontrados

    tiempo_busqueda_existentes = sum(tiempos) / len(tiempos)
    print(f"{Fore.WHITE}Búsqueda de 10 IDs existentes: {Fore.GREEN}{tiempo_busqueda_existentes:.3f} ms "
          f"{Fore.WHITE}(encontrados: {encontrados_existentes}/10)")

    # Buscar IDs no existentes
    id_max = max(p.id for p in productos)
    ids_no_existentes = [id_max + i + 1 for i in range(10)]
    tiempos = []
    encontrados_no_existentes = 0

    for _ in range(20):  # Repetir para obtener mediciones más precisas
        inicio_tiempo = time.perf_counter()
        encontrados = 0
        for id in ids_no_existentes:
            producto = sistema_busqueda.buscar_por_id(id)
            if producto:
                encontrados += 1
        fin_tiempo = time.perf_counter()
        tiempos.append((fin_tiempo - inicio_tiempo) * 1000)
        encontrados_no_existentes = encontrados

    tiempo_busqueda_no_existentes = sum(tiempos) / len(tiempos)
    print(f"{Fore.WHITE}Búsqueda de 10 IDs no existentes: {Fore.GREEN}{tiempo_busqueda_no_existentes:.3f} ms "
          f"{Fore.WHITE}(encontrados: {encontrados_no_existentes}/10)")

    # Búsqueda lineal de productos por nombre
    print(f"\n{Fore.YELLOW}Búsqueda por Nombre:")

    # Generar subcadenas existentes
    subcadenas_existentes = []
    for _ in range(10):
        producto = random.choice(productos)
        palabras = producto.nombre.split()
        if palabras:
            subcadena = random.choice(palabras)
            subcadenas_existentes.append(subcadena)

    # Mostrar subcadenas generadas
    print(f"{Fore.WHITE}Subcadenas existentes generadas: {', '.join(subcadenas_existentes)}")

    # Benchmark de diferentes métodos de búsqueda por nombre
    print(f"\n{Fore.CYAN}Comparación de Métodos de Búsqueda por Nombre:")

    # Comparar métodos para subcadenas existentes
    print(f"\n{Fore.YELLOW}Subcadenas existentes:")
    resultados_existentes = sistema_busqueda.comparar_metodos_busqueda(subcadenas_existentes[:5])

    # Subcadenas no existentes
    subcadenas_no_existentes = ["xyz123", "qwerty", "noexiste", "productofake", "itemfalso"]
    print(f"\n{Fore.WHITE}Subcadenas no existentes utilizadas: {', '.join(subcadenas_no_existentes)}")

    # Comparar métodos para subcadenas no existentes
    print(f"\n{Fore.YELLOW}Subcadenas no existentes:")
    resultados_no_existentes = sistema_busqueda.comparar_metodos_busqueda(subcadenas_no_existentes)

    # Visualizar comparación de métodos de búsqueda
    visualizar_comparacion_metodos_busqueda(resultados_existentes, resultados_no_existentes)

    # Búsqueda lineal por nombre tradicional (para comparar con métodos avanzados)
    # Buscar subcadenas existentes
    tiempos = []
    encontrados_nombre_existentes = 0
    total_coincidencias_existentes = 0

    for _ in range(5):  # Repetir para obtener un promedio más preciso
        inicio_tiempo = time.perf_counter()
        encontrados = 0
        total_coincidencias = 0
        for subcadena in subcadenas_existentes:
            coincidencias = busqueda_lineal_por_nombre(productos, subcadena)
            if coincidencias:
                encontrados += 1
            total_coincidencias += len(coincidencias)
        fin_tiempo = time.perf_counter()
        tiempos.append((fin_tiempo - inicio_tiempo) * 1000)
        encontrados_nombre_existentes = encontrados
        total_coincidencias_existentes = total_coincidencias

    tiempo_busqueda_nombre_existentes = sum(tiempos) / len(tiempos)
    print(
        f"\n{Fore.WHITE}Búsqueda lineal de 10 subcadenas existentes: {Fore.GREEN}{tiempo_busqueda_nombre_existentes:.3f} ms "
        f"{Fore.WHITE}(búsquedas con resultados: {encontrados_nombre_existentes}/10, coincidencias totales: {total_coincidencias_existentes})")

    # Buscar subcadenas no existentes
    tiempos = []
    encontrados_nombre_no_existentes = 0
    total_coincidencias_no_existentes = 0

    for _ in range(5):  # Repetir para obtener un promedio más preciso
        inicio_tiempo = time.perf_counter()
        encontrados = 0
        total_coincidencias = 0
        for subcadena in subcadenas_no_existentes:
            coincidencias = busqueda_lineal_por_nombre(productos, subcadena)
            if coincidencias:
                encontrados += 1
            total_coincidencias += len(coincidencias)
        fin_tiempo = time.perf_counter()
        tiempos.append((fin_tiempo - inicio_tiempo) * 1000)
        encontrados_nombre_no_existentes = encontrados
        total_coincidencias_no_existentes = total_coincidencias

    tiempo_busqueda_nombre_no_existentes = sum(tiempos) / len(tiempos)

    print(
        f"{Fore.WHITE}Búsqueda lineal de 5 subcadenas no existentes: {Fore.GREEN}{tiempo_busqueda_nombre_no_existentes:.3f} ms "
        f"{Fore.WHITE}(búsquedas con resultados: {encontrados_nombre_no_existentes}/5, coincidencias totales: {total_coincidencias_no_existentes})")

    # Crear visualización para algoritmos de búsqueda
    resultados_busqueda = [
        {
            'nombre': 'Búsqueda Binaria',
            'detalle': 'IDs existentes',
            'tiempo_ms': tiempo_busqueda_existentes,
            'exitosas': encontrados_existentes,
            'total_resultados': encontrados_existentes
        },
        {
            'nombre': 'Búsqueda Binaria',
            'detalle': 'IDs no existentes',
            'tiempo_ms': tiempo_busqueda_no_existentes,
            'exitosas': encontrados_no_existentes,
            'total_resultados': encontrados_no_existentes
        },
        {
            'nombre': 'Búsqueda Lineal',
            'detalle': 'Nombres existentes',
            'tiempo_ms': tiempo_busqueda_nombre_existentes,
            'exitosas': encontrados_nombre_existentes,
            'total_resultados': total_coincidencias_existentes
        },
        {
            'nombre': 'Búsqueda Lineal',
            'detalle': 'Nombres no existentes',
            'tiempo_ms': tiempo_busqueda_nombre_no_existentes,
            'exitosas': encontrados_nombre_no_existentes,
            'total_resultados': total_coincidencias_no_existentes
        }
    ]

    # Visualizar rendimiento de búsqueda
    visualizar_rendimiento_busqueda(
        resultados_busqueda,
        "Comparación de Algoritmos de Búsqueda",
        "rendimiento_busqueda.png"
    )

    # Mostrar todos los productos generados
    print(f"\n{Fore.YELLOW}Lista completa de todos los {len(productos)} productos generados:")
    datos_completos = [[p.id, p.nombre, f"${p.precio:.2f}", p.categoria, p.stock, p.calificacion_promedio]
                       for p in productos]

    # Generar PDF con la lista completa de productos
    print(f"\n{Fore.YELLOW}Generando PDF con la lista completa de productos...")
    archivo_pdf = generar_pdf_productos(productos)
    print(f"{Fore.GREEN}✓ PDF generado exitosamente: '{archivo_pdf}'")

    # Mostrar primeros 20 y últimos 20 productos para no saturar la consola
    print(f"\n{Fore.CYAN}Primeros 20 productos:")
    print(generar_tabla(datos_completos[:20],["ID", "Nombre", "Precio", "Categoría", "Stock", "Calificación"]))

    print(f"\n{Fore.CYAN}Últimos 20 productos:")
    print(generar_tabla(datos_completos[-20:],["ID", "Nombre", "Precio", "Categoría", "Stock", "Calificación"]))

    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}{'ANÁLISIS COMPLETADO':^60}")
    print(f"{Fore.CYAN}{'=' * 60}")

if __name__ == "__main__":
    main()