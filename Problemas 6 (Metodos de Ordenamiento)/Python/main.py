# Realice los programas de ordenamiento de burbuja y de Selección en los lenguajes C++, Java y Python, muestre la impresión de pantalla para cada uno de ellos.
# En que se diferencia y en que se asemejan cada uno de los métodos?

import time
from colorama import init, Fore, Style
from tabulate import tabulate

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
        if mas_pequeno != actual:  # Corregido de "min is not actual"
            temp = vector_copy[actual]
            vector_copy[actual] = vector_copy[mas_pequeno]
            vector_copy[mas_pequeno] = temp
        steps.append([f"Iteración {actual + 1}", vector_copy.copy()])

    return vector_copy, steps


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
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Salir")
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
                print(f"{Fore.GREEN}Comparando ambos algoritmos...{Style.RESET_ALL}")

                # Medir tiempo para bubble sort
                start_time = time.time()
                bubble_sorted, bubble_steps = bubble_sort(vector)
                bubble_time = time.time() - start_time

                # Medir tiempo para selection sort
                start_time = time.time()
                selection_sorted, selection_steps = selection_sort(vector)
                selection_time = time.time() - start_time

                # Mostrar resultados
                print(f"\n{Fore.GREEN}=== Comparación de Algoritmos ==={Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Vector original: {Style.RESET_ALL}{vector}")

                comparison = [
                    ["Burbuja", len(bubble_steps) - 1, f"{bubble_time:.6f} segundos"],
                    ["Selección", len(selection_steps) - 1, f"{selection_time:.6f} segundos"]
                ]

                print(tabulate(comparison,headers=["Algoritmo", "Iteraciones", "Tiempo de ejecución"], tablefmt="grid"))

                if bubble_time < selection_time:
                    print(f"{Fore.GREEN}El algoritmo de burbuja fue más rápido para este vector.{Style.RESET_ALL}")
                elif selection_time < bubble_time:
                    print(f"{Fore.GREEN}El algoritmo de selección fue más rápido para este vector.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}Ambos algoritmos tomaron el mismo tiempo.{Style.RESET_ALL}")

                press_to_continue()

            elif opcion == 4:
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