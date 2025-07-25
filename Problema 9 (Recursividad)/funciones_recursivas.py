# 1. Suma de los n primeros números naturales
def suma_naturales(n):
    if n <= 1:
        return n
    return n + suma_naturales(n - 1)

# 2. Números entre a y d
def imprimir_entre(a, d):
    if a > d:
        return
    print(a, end=" ")
    imprimir_entre(a + 1, d)

# 3. Cantidad de dígitos de un número
def contar_digitos(n):
    if abs(n) < 10:
        return 1
    return 1 + contar_digitos(abs(n) // 10)

# 4. Potencia mediante multiplicaciones
def potencia(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / potencia(x, -y)
    return x * potencia(x, y - 1)

# 5. Multiplicación mediante sumas
def multiplicar(x, y):
    if y == 0:
        return 0
    elif y < 0:
        return -multiplicar(x, -y)
    return x + multiplicar(x, y - 1)

# 6. Valor máximo de un vector
def maximo(vector, n):
    if n == 1:
        return vector[0]
    return max(vector[n-1], maximo(vector, n-1))

# 7. Contar secuencias de dos 1 seguidos
def contar_unos_seguidos(binario, indice=0):
    if indice >= len(binario) - 1:
        return 0
    if binario[indice] == '1' and binario[indice + 1] == '1':
        return 1 + contar_unos_seguidos(binario, indice + 1)
    return contar_unos_seguidos(binario, indice + 1)

# 8. Hexadecimal a decimal
def hexa_a_decimal(hexa, indice=0):
    if indice >= len(hexa):
        return 0

    digito = hexa[indice].upper()
    if '0' <= digito <= '9':
        valor = int(digito)
    else:
        valor = ord(digito) - ord('A') + 10

    potencia = len(hexa) - indice - 1
    return valor * (16 ** potencia) + hexa_a_decimal(hexa, indice + 1)

# 9. Contar secuencias de m unos consecutivos
def contar_m_unos_seguidos(binario, m, indice=0):
    if indice > len(binario) - m:
        return 0

    es_secuencia = True
    for i in range(m):
        if indice + i >= len(binario) or binario[indice + i] != '1':
            es_secuencia = False
            break

    if es_secuencia:
        return 1 + contar_m_unos_seguidos(binario, m, indice + 1)
    return contar_m_unos_seguidos(binario, m, indice + 1)

# 10. Coeficiente binomial
def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    return coeficiente_binomial(n-1, k-1) + coeficiente_binomial(n-1, k)

def main():
    print(f"Suma de los primeros 5 números: {suma_naturales(5)}")

    print("\nNúmeros entre 5 y 10: ", end="")
    imprimir_entre(5, 10)

    print(f"\n\nDígitos en 12345: {contar_digitos(12345)}")
    print(f"2^5 = {potencia(2, 5)}")
    print(f"5*3 = {multiplicar(5, 3)}")

    vector = [3, 10, 2, 8, 5]
    print(f"Máximo en el vector {vector}: {maximo(vector, len(vector))}")

    binario = "10110111"
    print(f"Secuencias de dos 1 en {binario}: {contar_unos_seguidos(binario)}")

    hexa = "1A3"
    print(f"Valor decimal de {hexa}: {hexa_a_decimal(hexa)}")

    binario = "10111011"
    print(f"Secuencias de tres 1 en {binario}: {contar_m_unos_seguidos(binario, 3)}")

    print(f"C(5,2) = {coeficiente_binomial(5, 2)}")

if __name__ == "__main__":
    main()