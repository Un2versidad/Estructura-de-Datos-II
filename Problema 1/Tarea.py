def imprimir_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Hola mundo")
    print("2. Suma de dos números")
    print("3. Conversión de temperatura")
    print("4. Área de un triángulo")
    print("5. Número par o impar")
    print("6. Mayor de tres números")
    print("7. Tabla de multiplicar")
    print("8. Contador regresivo")
    print("9. Suma de números del 1 al N")
    print("10. Calculadora simple")
    print("11. Función de factorial")
    print("12. Número primo")
    print("13. Conversión de minutos a horas y minutos")
    print("0. Salir")

def hola_mundo():
    print("Hola, mundo")

def suma_dos_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {num1 + num2}")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

def conversion_temperatura():
    opcion = input("Convertir (C)elsius a Fahrenheit o (F)ahrenheit a Celsius? ").upper()
    if opcion == "C":
        try:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C equivale a {fahrenheit}°F")
        except ValueError:
            print("Entrada inválida.")
    elif opcion == "F":
        try:
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")
        except ValueError:
            print("Entrada inválida.")
    else:
        print("Opción no válida.")

def area_triangulo():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    except ValueError:
        print("Entrada inválida.")

def numero_par_impar():
    try:
        numero = int(input("Ingrese un número: "))
        if numero % 2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
        print("Entrada inválida.")

def mayor_de_tres_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))
        mayor = max(num1, num2, num3)
        print(f"El mayor número es: {mayor}")
    except ValueError:
        print("Entrada inválida.")

def tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Entrada inválida.")

def contador_regresivo():
    numero = 10
    while numero >= 1:
        print(numero)
        numero -= 1

def suma_hasta_n():
    try:
        n = int(input("Ingrese un número: "))
        suma = sum(range(1, n + 1))
        print(f"La suma de los números del 1 al {n} es: {suma}")
    except ValueError:
        print("Entrada inválida.")

def calculadora_simple():
    try:
        num1 = float(input("Ingrese el primer número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))
        if operacion == "+":
            print(f"Resultado: {num1 + num2}")
        elif operacion == "-":
            print(f"Resultado: {num1 - num2}")
        elif operacion == "*":
            print(f"Resultado: {num1 * num2}")
        elif operacion == "/":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: División por cero.")
        else:
            print("Operación no válida.")
    except ValueError:
        print("Entrada inválida.")

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)

def funcion_factorial():
    try:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        if numero < 0:
            print("No se puede calcular el factorial de un número negativo.")
        else:
            print(f"El factorial de {numero} es: {factorial(numero)}")
    except ValueError:
        print("Entrada inválida.")

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numero_primo():
    try:
        numero = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(numero):
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")
    except ValueError:
        print("Entrada inválida.")

def conversion_minutos():
    try:
        minutos = int(input("Ingrese la cantidad de minutos: "))
        horas = minutos // 60
        minutos_restantes = minutos % 60
        print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")
    except ValueError:
        print("Entrada inválida.")

# Programa principal
while True:
    imprimir_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hola_mundo()
    elif opcion == "2":
        suma_dos_numeros()
    elif opcion == "3":
        conversion_temperatura()
    elif opcion == "4":
        area_triangulo()
    elif opcion == "5":
        numero_par_impar()
    elif opcion == "6":
        mayor_de_tres_numeros()
    elif opcion == "7":
        tabla_multiplicar()
    elif opcion == "8":
        contador_regresivo()
    elif opcion == "9":
        suma_hasta_n()
    elif opcion == "10":
        calculadora_simple()
    elif opcion == "11":
        funcion_factorial()
    elif opcion == "12":
        numero_primo()
    elif opcion == "13":
        conversion_minutos()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")