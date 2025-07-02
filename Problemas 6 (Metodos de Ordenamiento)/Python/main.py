# Realice los programas de ordenamiento de burbuja y de Selección en los lenguajes C++, Java y Python, muestre la impresión de pantalla para cada uno de ellos.
# En que se diferencia y en que se asemejan cada uno de los métodos?

import time
import random
from colorama import init, Fore, Style
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

def bubble_sort(vector):
    """Implementación del algoritmo de ordenamiento burbuja."""
    vector_copy = vector.copy()
    permutation = True
    iteracion = 0
    steps = [["Inicial", vector_copy.copy()]]

    while permutation:
        permutation = False
        iteracion = iteracion + 1
        for actual in range(0, len(vector_copy) - iteracion):
            if vector_copy[actual] > vector_copy[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector_copy[actual], vector_copy[actual + 1] = vector_copy[actual + 1], vector_copy[actual]
        steps.append([f"Iteración {iteracion}", vector_copy.copy()])

    return vector_copy, steps

def selection_sort(vector):
    """Implementación del algoritmo de ordenamiento por selección."""
    vector_copy = vector.copy()
    nb = len(vector_copy)
    steps = [["Inicial", vector_copy.copy()]]

    for actual in range(0, nb):
        mas_pequeno = actual
        for j in range(actual + 1, nb):
            if vector_copy[j] < vector_copy[mas_pequeno]:
                mas_pequeno = j
        if mas_pequeno != actual:
            temp = vector_copy[actual]
            vector_copy[actual] = vector_copy[mas_pequeno]
            vector_copy[mas_pequeno] = temp
        steps.append([f"Iteración {actual + 1}", vector_copy.copy()])

    return vector_copy, steps

def measure_execution_time(sort_function, vector, repetitions=10):
    """Mide el tiempo de ejecución con mayor precisión."""
    times = []
    sorted_result = None
    steps = None

    for _ in range(repetitions):
        vector_copy = vector.copy()
        start_time = time.perf_counter()
        sorted_result, steps = sort_function(vector_copy)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return sum(times) / len(times), sorted_result, steps

def get_valid_vector():
    """Solicita al usuario ingresar un vector válido de números."""
    while True:
        try:
            input_str = input(f"{Fore.CYAN}Ingrese los números separados por espacio: {Style.RESET_ALL}")
            vector = list(map(int, input_str.split()))
            if not vector:
                print(f"{Fore.RED}Error: Debe ingresar al menos un número.{Style.RESET_ALL}")
                continue
            return vector
        except ValueError:
            print(f"{Fore.RED}Error: Ingrese solo números enteros válidos.{Style.RESET_ALL}")

def generate_random_vector(size=20, min_val=1, max_val=100):
    """Genera un vector aleatorio de números enteros."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def compare_algorithms(vector):
    """Compara los algoritmos de ordenamiento y muestra los resultados."""
    print(f"{Fore.GREEN}Comparando ambos algoritmos...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Ejecutando mediciones precisas (puede tomar unos segundos)...{Style.RESET_ALL}")

    # Medir tiempo para bubble sort
    bubble_time, bubble_sorted, bubble_steps = measure_execution_time(bubble_sort, vector)

    # Medir tiempo para selection sort
    selection_time, selection_sorted, selection_steps = measure_execution_time(selection_sort, vector)

    # Mostrar resultados
    print(f"\n{Fore.GREEN}=== Comparación de Algoritmos ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Vector original: {Style.RESET_ALL}{vector}")

    comparison = [
        ["Burbuja", len(bubble_steps) - 1, f"{bubble_time:.4f} milisegundos"],
        ["Selección", len(selection_steps) - 1, f"{selection_time:.4f} milisegundos"]
    ]

    print(tabulate(comparison,headers=["Algoritmo", "Iteraciones", "Tiempo de ejecución"],tablefmt="grid"))

    if bubble_time < selection_time:
        print(f"{Fore.GREEN}El algoritmo de burbuja fue más rápido para este vector.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Diferencia: {selection_time - bubble_time:.4f} milisegundos{Style.RESET_ALL}")
    elif selection_time < bubble_time:
        print(f"{Fore.GREEN}El algoritmo de selección fue más rápido para este vector.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Diferencia: {bubble_time - selection_time:.4f} milisegundos{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Ambos algoritmos tomaron el mismo tiempo.{Style.RESET_ALL}")

def press_to_continue():
    """Pausa el programa hasta que el usuario presione Enter."""
    input(f"\n{Fore.YELLOW}Presione Enter para continuar...{Style.RESET_ALL}")

def display_results(original, sorted_vector, steps, algorithm_name):
    """Muestra los resultados del ordenamiento en formato tabular."""
    print(f"\n{Fore.GREEN}=== Resultados del {algorithm_name} ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Vector original: {Style.RESET_ALL}{original}")
    print(f"{Fore.YELLOW}Vector ordenado: {Style.RESET_ALL}{sorted_vector}")

    print(f"\n{Fore.CYAN}Pasos del algoritmo:{Style.RESET_ALL}")
    print(tabulate(steps, headers=["Paso", "Estado del vector"], tablefmt="grid"))

def menu():
    """Muestra un menú interactivo para seleccionar el algoritmo de ordenamiento."""
    while True:
        print(f"\n{Fore.MAGENTA}{'=' * 40}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'ALGORITMOS DE ORDENAMIENTO':^40}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'=' * 40}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Ordenamiento de Burbuja")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Ordenamiento por Selección")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Comparar ambos algoritmos")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Generar vector aleatorio")
        print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Salir")
        print(f"{Fore.MAGENTA}{'-' * 40}{Style.RESET_ALL}")

        try:
            opcion = int(input(f"{Fore.CYAN}Seleccione una opción: {Style.RESET_ALL}"))

            if opcion == 1:
                vector = get_valid_vector()
                print(f"{Fore.GREEN}Ordenando con algoritmo de burbuja...{Style.RESET_ALL}")
                sorted_vector, steps = bubble_sort(vector)
                display_results(vector, sorted_vector, steps, "Ordenamiento de Burbuja")
                press_to_continue()

            elif opcion == 2:
                vector = get_valid_vector()
                print(f"{Fore.GREEN}Ordenando con algoritmo de selección...{Style.RESET_ALL}")
                sorted_vector, steps = selection_sort(vector)
                display_results(vector, sorted_vector, steps, "Ordenamiento por Selección")
                press_to_continue()

            elif opcion == 3:
                vector = get_valid_vector()
                compare_algorithms(vector)
                press_to_continue()

            elif opcion == 4:
                try:
                    size = int(input(f"{Fore.CYAN}Ingrese el tamaño del vector aleatorio: {Style.RESET_ALL}"))
                    if size <= 0:
                        print(f"{Fore.RED}Error: El tamaño debe ser un número positivo.{Style.RESET_ALL}")
                        continue

                    min_val = int(input(f"{Fore.CYAN}Ingrese el valor mínimo: {Style.RESET_ALL}"))
                    max_val = int(input(f"{Fore.CYAN}Ingrese el valor máximo: {Style.RESET_ALL}"))

                    if min_val >= max_val:
                        print(f"{Fore.RED}Error: El valor mínimo debe ser menor que el máximo.{Style.RESET_ALL}")
                        continue

                    vector = generate_random_vector(size, min_val, max_val)
                    print(f"{Fore.GREEN}Vector generado: {Style.RESET_ALL}{vector}")

                    # Preguntar qué hacer con el vector generado
                    print(f"\n{Fore.YELLOW}¿Qué desea hacer con este vector?{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Ordenar con Burbuja")
                    print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Ordenar con Selección")
                    print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Comparar ambos algoritmos")
                    print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Volver al menú principal")

                    sub_opcion = int(input(f"{Fore.CYAN}Seleccione una opción: {Style.RESET_ALL}"))

                    if sub_opcion == 1:
                        print(f"{Fore.GREEN}Ordenando con algoritmo de burbuja...{Style.RESET_ALL}")
                        sorted_vector, steps = bubble_sort(vector)
                        display_results(vector, sorted_vector, steps, "Ordenamiento de Burbuja")
                    elif sub_opcion == 2:
                        print(f"{Fore.GREEN}Ordenando con algoritmo de selección...{Style.RESET_ALL}")
                        sorted_vector, steps = selection_sort(vector)
                        display_results(vector, sorted_vector, steps, "Ordenamiento por Selección")
                    elif sub_opcion == 3:
                        compare_algorithms(vector)
                    elif sub_opcion == 4:
                        pass  # Volver al menú principal
                    else:
                        print(f"{Fore.RED}Opción no válida.{Style.RESET_ALL}")

                except ValueError:
                    print(f"{Fore.RED}Error: Ingrese valores numéricos válidos.{Style.RESET_ALL}")

                press_to_continue()

            elif opcion == 5:
                print(f"{Fore.GREEN}Saliendo del programa. ¡Hasta pronto!{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Opción no válida. Intente de nuevo.{Style.RESET_ALL}")
                press_to_continue()

        except ValueError:
            print(f"{Fore.RED}Error: Ingrese un número entero válido.{Style.RESET_ALL}")
            press_to_continue()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Programa interrumpido por el usuario.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Error inesperado: {e}{Style.RESET_ALL}")
