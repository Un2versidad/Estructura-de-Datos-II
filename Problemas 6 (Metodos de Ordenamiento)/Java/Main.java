import java.util.*;

public class Main {
    static List<String> bubbleSortSteps(int[] arr) {
        int[] a = arr.clone();
        List<String> steps = new ArrayList<>();
        steps.add("Inicial: " + Arrays.toString(a));
        boolean permutation = true;
        int iter = 0;
        while (permutation) {
            permutation = false;
            iter++;
            for (int i = 0; i < a.length - iter; i++) {
                if (a[i] > a[i + 1]) {
                    int temp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = temp;
                    permutation = true;
                }
            }
            steps.add("Iteración " + iter + ": " + Arrays.toString(a));
        }
        return steps;
    }

    static List<String> selectionSortSteps(int[] arr) {
        int[] a = arr.clone();
        List<String> steps = new ArrayList<>();
        steps.add("Inicial: " + Arrays.toString(a));
        for (int i = 0; i < a.length; i++) {
            int minIdx = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                int temp = a[i];
                a[i] = a[minIdx];
                a[minIdx] = temp;
            }
            steps.add("Iteración " + (i + 1) + ": " + Arrays.toString(a));
        }
        return steps;
    }

    static int[] getUserArray(Scanner scanner) {
        while (true) {
            System.out.print("Ingrese los números separados por espacio: ");
            String line = scanner.nextLine();
            String[] parts = line.trim().split("\\s+");
            try {
                int[] arr = new int[parts.length];
                for (int i = 0; i < parts.length; i++) {
                    arr[i] = Integer.parseInt(parts[i]);
                }
                return arr;
            } catch (NumberFormatException e) {
                System.out.println("Error: Ingrese solo números enteros válidos.");
            }
        }
    }

    static void printSteps(List<String> steps, String title) {
        System.out.println("\n=== Pasos del " + title + " ===");
        for (String step : steps) {
            System.out.println(step);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n===== ALGORITMOS DE ORDENAMIENTO =====");
            System.out.println("1. Ordenamiento de Burbuja");
            System.out.println("2. Ordenamiento por Selección");
            System.out.println("3. Comparar ambos algoritmos");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            String opStr = scanner.nextLine();
            int opcion;
            try {
                opcion = Integer.parseInt(opStr);
            } catch (NumberFormatException e) {
                System.out.println("Error: Ingrese un número entero válido.");
                continue;
            }
            if (opcion == 4) {
                System.out.println("Saliendo del programa. ¡Hasta pronto!");
                break;
            }
            int[] arr = getUserArray(scanner);
            if (opcion == 1) {
                System.out.println("\nOrdenando con algoritmo de burbuja...");
                List<String> steps = bubbleSortSteps(arr);
                printSteps(steps, "Ordenamiento de Burbuja");
            } else if (opcion == 2) {
                System.out.println("\nOrdenando con algoritmo de selección...");
                List<String> steps = selectionSortSteps(arr);
                printSteps(steps, "Ordenamiento por Selección");
            } else if (opcion == 3) {
                System.out.println("\nComparando ambos algoritmos...");
                long t1 = System.nanoTime();
                List<String> bubbleSteps = bubbleSortSteps(arr);
                long t2 = System.nanoTime();
                List<String> selectionSteps = selectionSortSteps(arr);
                long t3 = System.nanoTime();
                System.out.println("\n=== Comparación de Algoritmos ===");
                System.out.println("Vector original: " + Arrays.toString(arr));
                System.out.printf("Burbuja: %d iteraciones, %.3f milisegundos\n", bubbleSteps.size() - 1, (t2 - t1) / 1e6);
                System.out.printf("Selección: %d iteraciones, %.3f milisegundos\n", selectionSteps.size() - 1, (t3 - t2) / 1e6);
                if ((t2 - t1) < (t3 - t2)) {
                    System.out.println("El algoritmo de burbuja fue más rápido para este vector.");
                } else if ((t3 - t2) < (t2 - t1)) {
                    System.out.println("El algoritmo de selección fue más rápido para este vector.");
                } else {
                    System.out.println("Ambos algoritmos tomaron el mismo tiempo.");
                }
            } else {
                System.out.println("Opción no válida. Intente de nuevo.");
            }
            System.out.println("\nPresione Enter para continuar...");
            scanner.nextLine();
        }
    }
}
