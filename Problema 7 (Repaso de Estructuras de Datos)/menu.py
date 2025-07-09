from colorama import Fore, Style, init
from tabulate import tabulate
from Inventario.Operaciones import GestorInventario, Cliente

# Inicializar colorama
init()

class Producto:
    def __init__(self, nombre, codigo, cantidad, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

def main():
    inventario = GestorInventario()

    # Productos iniciales
    productos_iniciales = [
        Producto("Laptop", "TECH001", 10, 999.99),
        Producto("Smartphone", "TECH002", 20, 599.99),
        Producto("Auriculares", "TECH003", 30, 149.99),
        Producto("Teclado", "TECH004", 15, 89.99),
        Producto("Ratón", "TECH005", 25, 49.99)
    ]

    inventario.agregar_productos_iniciales(productos_iniciales)

    while True:
        print(Fore.CYAN + "\n===== Sistema de Gestión de Inventario =====" + Style.RESET_ALL)
        print("1. Mostrar inventario (por nombre)")
        print("2. Mostrar inventario (por precio)")
        print("3. Agregar producto")
        print("4. Eliminar producto")
        print("5. Editar producto")
        print("6. Buscar producto")
        print("7. Ver historial de operaciones")
        print("8. Deshacer última operación")
        print("9. Agregar pedido de cliente")
        print("10. Procesar siguiente pedido")
        print("11. Ver cola de pedidos")
        print("12. Ver productos (orden ABB)")
        print("13. Salir")

        opcion = input(Fore.YELLOW + "\nIngrese opción (1-13): " + Style.RESET_ALL)

        if opcion == '1':
            print(Fore.GREEN + "\nProductos ordenados por nombre:" + Style.RESET_ALL)
            productos = inventario.ordenar_por_nombre()
            datos = [[p.nombre, p.codigo, p.cantidad, f"${p.precio}"] for p in productos]
            print(tabulate(datos, headers=["Nombre", "Código", "Cantidad", "Precio"], tablefmt="grid"))

        elif opcion == '2':
            print(Fore.GREEN + "\nProductos ordenados por precio:" + Style.RESET_ALL)
            productos = inventario.ordenar_por_precio()
            datos = [[p.nombre, p.codigo, p.cantidad, f"${p.precio}"] for p in productos]
            print(tabulate(datos, headers=["Nombre", "Código", "Cantidad", "Precio"], tablefmt="grid"))

        elif opcion == '3':
            while True:
                nombre = input("Nombre: ")
                if not nombre.strip():
                    print(Fore.RED + "Error: El nombre del producto no puede estar vacío." + Style.RESET_ALL)
                    continue
                break

            while True:
                codigo = input("Código: ")
                if not codigo.strip():
                    print(Fore.RED + "Error: El código del producto no puede estar vacío." + Style.RESET_ALL)
                    continue

                if inventario.lista_enlazada.buscar(codigo):
                    print(Fore.RED + "Error: Ya existe un producto con ese código." + Style.RESET_ALL)
                    continue
                break

            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    if cantidad < 0:
                        print(Fore.RED + "Error: La cantidad no puede ser negativa." + Style.RESET_ALL)
                        continue
                    if cantidad > 100000:
                        print(Fore.RED + "Error: La cantidad parece excesivamente grande." + Style.RESET_ALL)
                        continue
                    break
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número entero válido." + Style.RESET_ALL)
            while True:
                try:
                    precio = float(input("Precio: "))
                    if precio <= 0:
                        print(Fore.RED + "Error: El precio debe ser mayor que cero." + Style.RESET_ALL)
                        continue
                    break
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
            inventario.agregar_producto(Producto(nombre, codigo, cantidad, precio))
            print(Fore.GREEN + "¡Producto agregado!" + Style.RESET_ALL)

        elif opcion == '4':
            codigo = input("Ingrese código del producto a eliminar: ")
            if inventario.eliminar_producto(codigo):
                print(Fore.GREEN + "¡Producto eliminado!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "¡Producto no encontrado!" + Style.RESET_ALL)

        elif opcion == '5':
            codigo = input("Ingrese código del producto a editar: ")
            producto = inventario.lista_enlazada.buscar(codigo)

            if producto:
                nuevos_datos = {}
                nombre = input(f"Nuevo nombre [{producto.nombre}] (o dejar en blanco): ")
                if nombre:
                    nuevos_datos['nombre'] = nombre

                cant = input(f"Nueva cantidad [{producto.cantidad}] (o dejar en blanco): ")
                if cant:
                    nuevos_datos['cantidad'] = int(cant)

                precio = input(f"Nuevo precio [{producto.precio}] (o dejar en blanco): ")
                if precio:
                    nuevos_datos['precio'] = float(precio)

                inventario.editar_producto(codigo, nuevos_datos)
                print(Fore.GREEN + "¡Producto actualizado!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "¡Producto no encontrado!" + Style.RESET_ALL)

        elif opcion == '6':
            busqueda = input("Ingrese código o nombre del producto a buscar: ")
            producto = inventario.lista_enlazada.buscar(busqueda)

            if producto:
                print(Fore.GREEN + f"Encontrado: {producto}" + Style.RESET_ALL)
            else:
                # Si no se encuentra por código, buscar por nombre
                resultados = inventario.lista_enlazada.buscar_por_nombre(busqueda)
                if resultados:
                    print(Fore.GREEN + f"Se encontraron {len(resultados)} productos:" + Style.RESET_ALL)
                    datos = [[p.nombre, p.codigo, p.cantidad, f"${p.precio}"] for p in resultados]
                    print(tabulate(datos, headers=["Nombre", "Código", "Cantidad", "Precio"], tablefmt="grid"))
                else:
                    print(Fore.RED + "¡Producto no encontrado!" + Style.RESET_ALL)

        elif opcion == '7':
            print(Fore.CYAN + "\nHistorial de Operaciones:" + Style.RESET_ALL)
            inventario.operaciones.mostrar()

        elif opcion == '8':
            if inventario.deshacer_ultima_operacion():
                print(Fore.GREEN + "¡Operación deshecha!" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "¡No hay operaciones para deshacer!" + Style.RESET_ALL)

        elif opcion == '9':

            nombre = input("Nombre del cliente: ")

            if not nombre.strip():
                print(Fore.RED + "Error: El nombre del cliente no puede estar vacío." + Style.RESET_ALL)
                continue

            productos = []

            while True:
                codigo = input("Código del producto (o 'listo'/'terminar' para finalizar): ")

                if codigo.lower() in ['listo', 'terminar']:
                    break

                producto = inventario.lista_enlazada.buscar(codigo)

                if not producto:
                    print(Fore.RED + "Error: El producto no existe en el inventario." + Style.RESET_ALL)
                    continue

                while True:
                    try:
                        cantidad = int(input("Cantidad: "))
                        if cantidad <= 0:
                            print(Fore.RED + "Error: La cantidad debe ser un número positivo." + Style.RESET_ALL)
                            continue

                        if cantidad > producto.cantidad:
                            print(
                                Fore.RED + f"Error: Solo hay {producto.cantidad} unidades disponibles." + Style.RESET_ALL)
                            continue
                        productos.append((codigo, cantidad))
                        break

                    except ValueError:
                        print(Fore.RED + "Error: Debe ingresar un número entero válido." + Style.RESET_ALL)

            if productos:
                inventario.agregar_pedido_cliente(Cliente(nombre, productos))
                print(Fore.GREEN + f"Pedido agregado para: {nombre}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "El pedido no contiene productos." + Style.RESET_ALL)

        elif opcion == '10':
            inventario.procesar_siguiente_pedido()

        elif opcion == '11':
            print(Fore.CYAN + "\nCola de Pedidos:" + Style.RESET_ALL)
            inventario.pedidos.mostrar()

        elif opcion == '12':
            print(Fore.CYAN + "\nProductos (Orden Inorden ABB):" + Style.RESET_ALL)
            productos = inventario.arbol_productos.inorden()
            datos = [[p.nombre, p.codigo, p.cantidad, f"${p.precio}"] for p in productos]
            print(tabulate(datos, headers=["Nombre", "Código", "Cantidad", "Precio"], tablefmt="grid"))

        elif opcion == '13':
            print(Fore.MAGENTA + "Saliendo del programa. ¡Adiós!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opción inválida. Por favor intente nuevamente." + Style.RESET_ALL)

if __name__ == "__main__":
    main()