#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <chrono>
#include <iomanip>
#include <locale.h>

using namespace std;

vector<string> bubbleSortSteps(const vector<int>& arr) {
    vector<int> a = arr;
    vector<string> steps;
    ostringstream oss;
    oss << "Inicial: [";
    for (size_t i = 0; i < a.size(); ++i) {
        oss << a[i];
        if (i + 1 < a.size()) oss << ", ";
    }
    oss << "]";
    steps.push_back(oss.str());

    bool permutation = true;
    int iter = 0;
    while (permutation) {
        permutation = false;
        iter++;
        for (size_t i = 0; i + 1 < a.size() - (iter - 1); ++i) {
            if (a[i] > a[i + 1]) {
                swap(a[i], a[i + 1]);
                permutation = true;
            }
        }
        ostringstream oss2;
        oss2 << "Iteración " << iter << ": [";
        for (size_t i = 0; i < a.size(); ++i) {
            oss2 << a[i];
            if (i + 1 < a.size()) oss2 << ", ";
        }
        oss2 << "]";
        steps.push_back(oss2.str());
    }
    return steps;
}

vector<string> selectionSortSteps(const vector<int>& arr) {
    vector<int> a = arr;
    vector<string> steps;
    ostringstream oss;
    oss << "Inicial: [";
    for (size_t i = 0; i < a.size(); ++i) {
        oss << a[i];
        if (i + 1 < a.size()) oss << ", ";
    }
    oss << "]";
    steps.push_back(oss.str());

    for (size_t i = 0; i < a.size(); ++i) {
        size_t minIdx = i;
        for (size_t j = i + 1; j < a.size(); ++j) {
            if (a[j] < a[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            swap(a[i], a[minIdx]);
        }
        ostringstream oss2;
        oss2 << "Iteración " << (i + 1) << ": [";
        for (size_t k = 0; k < a.size(); ++k) {
            oss2 << a[k];
            if (k + 1 < a.size()) oss2 << ", ";
        }
        oss2 << "]";
        steps.push_back(oss2.str());
    }
    return steps;
}

vector<int> getUserArray() {
    while (true) {
        cout << "Ingrese los números separados por espacio: ";
        string line;
        getline(cin, line);
        istringstream iss(line);
        vector<int> arr;
        int num;
        bool valid = true;
        while (iss >> num) {
            arr.push_back(num);
        }
        if (!arr.empty() && iss.eof()) {
            return arr;
        }
        else {
            cout << "Error: Ingrese solo números enteros válidos." << endl;
        }
    }
}

void printSteps(const vector<string>& steps, const string& title) {
    cout << "\n=== Pasos del " << title << " ===" << endl;
    for (const auto& step : steps) {
        cout << step << endl;
    }
}

int main() {
    setlocale(LC_ALL, "Spanish");
    while (true) {
        cout << "\n===== ALGORITMOS DE ORDENAMIENTO =====" << endl;
        cout << "1. Ordenamiento de Burbuja" << endl;
        cout << "2. Ordenamiento por Selección" << endl;
        cout << "3. Comparar ambos algoritmos" << endl;
        cout << "4. Salir" << endl;
        cout << "Seleccione una opción: ";
        string opStr;
        getline(cin, opStr);
        int opcion;
        try {
            opcion = stoi(opStr);
        }
        catch (...) {
            cout << "Error: Ingrese un número entero válido." << endl;
            continue;
        }
        if (opcion == 4) {
            cout << "Saliendo del programa. ¡Hasta pronto!" << endl;
            break;
        }
        vector<int> arr = getUserArray();
        if (opcion == 1) {
            cout << "\nOrdenando con algoritmo de burbuja..." << endl;
            vector<string> steps = bubbleSortSteps(arr);
            printSteps(steps, "Ordenamiento de Burbuja");
        }
        else if (opcion == 2) {
            cout << "\nOrdenando con algoritmo de selección..." << endl;
            vector<string> steps = selectionSortSteps(arr);
            printSteps(steps, "Ordenamiento por Selección");
        }
        else if (opcion == 3) {
            cout << "\nComparando ambos algoritmos..." << endl;
            auto t1 = chrono::high_resolution_clock::now();
            vector<string> bubbleSteps = bubbleSortSteps(arr);
            auto t2 = chrono::high_resolution_clock::now();
            vector<string> selectionSteps = selectionSortSteps(arr);
            auto t3 = chrono::high_resolution_clock::now();
            cout << "\n=== Comparación de Algoritmos ===" << endl;
            cout << "Vector original: [";
            for (size_t i = 0; i < arr.size(); ++i) {
                cout << arr[i];
                if (i + 1 < arr.size()) cout << ", ";
            }
            cout << "]" << endl;
            double bubbleTime = chrono::duration<double, std::milli>(t2 - t1).count();
            double selectionTime = chrono::duration<double, std::milli>(t3 - t2).count();
            cout << fixed << setprecision(3);
            cout << "Burbuja: " << (bubbleSteps.size() - 1) << " iteraciones, " << bubbleTime << " ms" << endl;
            cout << "Selección: " << (selectionSteps.size() - 1) << " iteraciones, " << selectionTime << " ms" << endl;
            if (bubbleTime < selectionTime) {
                cout << "El algoritmo de burbuja fue más rápido para este vector." << endl;
            }
            else if (selectionTime < bubbleTime) {
                cout << "El algoritmo de selección fue más rápido para este vector." << endl;
            }
            else {
                cout << "Ambos algoritmos tomaron el mismo tiempo." << endl;
            }
        }
        else {
            cout << "Opción no válida. Intente de nuevo." << endl;
        }
        cout << "\nPresione Enter para continuar...";
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    return 0;
}
