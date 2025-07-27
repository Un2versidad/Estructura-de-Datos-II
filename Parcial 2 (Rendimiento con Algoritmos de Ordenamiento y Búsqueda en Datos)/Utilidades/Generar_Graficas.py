import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore
import numpy as np
from matplotlib.ticker import MaxNLocator

# Funciones de visualización
def visualizar_rendimiento_ordenamiento(resultados, titulo, archivo):
    """
    Genera visualización detallada del rendimiento de algoritmos de ordenamiento.

    Args:
        resultados: Lista de diccionarios con datos de rendimiento
        titulo: Título del gráfico
        archivo: Nombre del archivo para guardar la imagen
    """
    # Crear DataFrame para visualización
    df = pd.DataFrame(resultados)

    # Configurar el estilo
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 7))

    # Crear gráfico de barras agrupadas
    ax = sns.barplot(x='algoritmo', y='tiempo_ms', hue='criterio', data=df, palette='viridis')

    # Añadir etiquetas de valores con formato adecuado
    for container in ax.containers:
        for bar in container:
            valor = bar.get_height()
            if valor > 0.01:
                ax.annotate(f'{valor:.2f} ms',
                            (bar.get_x() + bar.get_width() / 2., valor),
                            ha='center', va='bottom', fontsize=9)
            elif valor > 0.001:
                ax.annotate(f'{valor:.3f} ms',
                            (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                            ha='center', va='bottom', fontsize=9)
            elif valor > 0:
                ax.annotate('<0.01 ms',
                            (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                            ha='center', va='bottom', fontsize=9)
            # No etiqueta si valor == 0

    # Configurar título y etiquetas
    plt.title(titulo, fontsize=16, pad=20)
    plt.xlabel('Algoritmo de Ordenamiento', fontsize=13)
    plt.ylabel('Tiempo (ms)', fontsize=13)
    plt.legend(title='Criterio de Ordenamiento', title_fontsize=12, fontsize=10)

    # Ajustar diseño
    plt.tight_layout()
    plt.savefig(archivo, dpi=300, bbox_inches='tight')
    print(f"{Fore.GREEN}✓ Gráfico de ordenamiento guardado como '{archivo}'")
    plt.close()  # Cerrar la figura para liberar memoria

def visualizar_rendimiento_busqueda(resultados_busqueda, titulo, archivo):
    """
    Genera visualización del rendimiento de los algoritmos de búsqueda.

    Args:
        resultados_busqueda: Lista de diccionarios con datos de búsqueda
        titulo: Título del gráfico
        archivo: Nombre del archivo para guardar la imagen
    """
    # Preparar datos
    nombres = [r['nombre'] for r in resultados_busqueda]
    detalles = [r['detalle'] for r in resultados_busqueda]
    tiempos = [r['tiempo_ms'] for r in resultados_busqueda]
    exitosas = [r['exitosas'] for r in resultados_busqueda]
    total_resultados = [r['total_resultados'] for r in resultados_busqueda]

    # Crear DataFrame
    df = pd.DataFrame({
        'Método de Búsqueda': nombres,
        'Detalle': detalles,
        'Tiempo (ms)': tiempos,
        'Búsquedas Exitosas': exitosas,
        'Resultados Totales': total_resultados
    })

    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico de tiempos
    sns.barplot(x='Método de Búsqueda', y='Tiempo (ms)', hue='Detalle', data=df, ax=ax1, palette='coolwarm')
    ax1.set_title('Tiempo de Ejecución', fontsize=14)
    ax1.set_ylabel('Tiempo (ms)', fontsize=12)
    ax1.set_xlabel('')

    # Añadir etiquetas de valores con formato adecuado
    for bar in ax1.patches:
        valor = bar.get_height()
        if valor > 0.01:
            ax1.annotate(f'{valor:.2f} ms',
                         (bar.get_x() + bar.get_width() / 2., valor),
                         ha='center', va='bottom', fontsize=9, rotation=0)
        elif valor > 0.001:
            ax1.annotate(f'{valor:.3f} ms',
                         (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                         ha='center', va='bottom', fontsize=9, rotation=0)
        elif valor > 0:
            ax1.annotate('<0.01 ms',
                         (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                         ha='center', va='bottom', fontsize=9, rotation=0)
        # No etiqueta si valor == 0

    # Gráfico de efectividad
    ind = np.arange(len(nombres) // 2)
    width = 0.35

    # Separar datos por tipo de búsqueda
    exitosas_existentes = exitosas[:len(exitosas) // 2]
    exitosas_no_existentes = exitosas[len(exitosas) // 2:]

    # Crear barras para la efectividad
    ax2.bar(ind - width / 2, exitosas_existentes, width, label='Existentes', color='forestgreen')
    ax2.bar(ind + width / 2, exitosas_no_existentes, width, label='No Existentes', color='firebrick')

    # Configurar eje X con nombres de métodos
    ax2.set_xticks(ind)
    ax2.set_xticklabels([n.split()[0] for n in nombres[:len(nombres) // 2]])
    ax2.set_title('Efectividad de Búsqueda', fontsize=14)
    ax2.set_ylabel('Búsquedas Exitosas', fontsize=12)
    ax2.set_ylim(0, 10)
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.legend()

    # Añadir etiquetas numéricas
    for i, v in enumerate(exitosas_existentes):
        ax2.text(i - width / 2, v + 0.1, str(v), ha='center', va='bottom', fontsize=9)
    for i, v in enumerate(exitosas_no_existentes):
        ax2.text(i + width / 2, v + 0.1, str(v), ha='center', va='bottom', fontsize=9)

    # Ajustar y guardar
    plt.suptitle(titulo, fontsize=16, y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.savefig(archivo, dpi=300, bbox_inches='tight')
    print(f"{Fore.GREEN}✓ Gráfico de búsqueda guardado como '{archivo}'")
    plt.close()  # Cerrar la figura para liberar memoria

def visualizar_comparacion_metodos_busqueda(resultados_existentes, resultados_no_existentes):
    """
    Genera visualización comparativa de diferentes métodos de búsqueda.

    Args:
        resultados_existentes: Diccionario con resultados para búsquedas existentes
        resultados_no_existentes: Diccionario con resultados para búsquedas no existentes
    """
    metodos = list(resultados_existentes.keys())

    # Calcular promedios
    promedios_existentes = {metodo: sum(t for t, _ in tiempos) / max(len(tiempos), 1)
                            for metodo, tiempos in resultados_existentes.items()}

    promedios_no_existentes = {metodo: sum(t for t, _ in tiempos) / max(len(tiempos), 1)
                               for metodo, tiempos in resultados_no_existentes.items()}

    # Crear DataFrame
    df = pd.DataFrame({
        'Método': metodos + metodos,
        'Tipo': ['Subcadenas Existentes'] * len(metodos) + ['Subcadenas No Existentes'] * len(metodos),
        'Tiempo Promedio (ms)': list(promedios_existentes.values()) + list(promedios_no_existentes.values())
    })

    # Crear gráfico
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")
    ax = sns.barplot(x='Método', y='Tiempo Promedio (ms)', hue='Tipo', data=df, palette='viridis')

    # Añadir etiquetas con formato adecuado
    for bar in ax.patches:
        valor = bar.get_height()
        if valor > 0.01:
            ax.annotate(f'{valor:.2f} ms',
                        (bar.get_x() + bar.get_width() / 2., valor),
                        ha='center', va='bottom', fontsize=10, rotation=0, xytext=(0, 5), textcoords='offset points')
        elif valor > 0.001:
            ax.annotate(f'{valor:.3f} ms',
                        (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                        ha='center', va='bottom', fontsize=10, rotation=0, xytext=(0, 5), textcoords='offset points')
        elif valor > 0:
            ax.annotate('<0.01 ms',
                        (bar.get_x() + bar.get_width() / 2., valor + 0.01),
                        ha='center', va='bottom', fontsize=10, rotation=0, xytext=(0, 5), textcoords='offset points') # No etiqueta si valor == 0

    plt.title('Comparación de Métodos de Búsqueda por Nombre', fontsize=16, pad=20)
    plt.xlabel('Método de Búsqueda', fontsize=13)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=13)
    plt.legend(title='Tipo de Búsqueda', title_fontsize=12, fontsize=10)

    plt.tight_layout()
    plt.savefig('comparacion_metodos_busqueda.png', dpi=300, bbox_inches='tight')
    print(f"{Fore.GREEN}✓ Gráfico de comparación de métodos guardado como 'comparacion_metodos_busqueda.png'")
    plt.close()  # Cerrar la figura para liberar memoria