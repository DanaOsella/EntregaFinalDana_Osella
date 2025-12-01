# Sistema de Gestión Básica de Productos
# Pre-Entrega del Proyecto - Python Inicial

def mostrar_menu():
    """Muestra el menú de opciones del sistema"""
    print("\n" + "="*40)
    print("SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("="*40)

def agregar_producto(productos):
    """Permite ingresar un nuevo producto a la lista"""
    print("\n--- AGREGAR PRODUCTO ---")
    
    # Validación del nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        else:
            print("Error: El nombre no puede estar vacío. Intente nuevamente.")
    
    # Validación de la categoría
    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        else:
            print("Error: La categoría no puede estar vacía. Intente nuevamente.")
    
    # Validación del precio
    while True:
        try:
            precio = int(input("Ingrese el precio del producto (sin centavos): "))
            if precio >= 0:
                break
            else:
                print("Error: El precio debe ser un número positivo. Intente nuevamente.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para el precio.")
    
    # Crear la sublista del producto y agregarla a la lista principal
    producto = [nombre, categoria, precio]
    productos.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.")

def mostrar_productos(productos):
    """Muestra todos los productos registrados de forma ordenada"""
    print("\n--- PRODUCTOS REGISTRADOS ---")
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print(f"{'No.':<4} {'Nombre':<20} {'Categoría':<15} {'Precio':<10}")
    print("-" * 55)
    
    for i, producto in enumerate(productos, 1):
        nombre, categoria, precio = producto
        print(f"{i:<4} {nombre:<20} {categoria:<15} ${precio:<9}")

def buscar_producto(productos):
    """Busca productos por nombre y muestra los resultados"""
    print("\n--- BUSCAR PRODUCTO ---")
    
    if not productos:
        print("No hay productos registrados para buscar.")
        return
    
    termino_busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    
    if not termino_busqueda:
        print("Error: Debe ingresar un término de búsqueda.")
        return
    
    resultados = []
    for producto in productos:
        nombre, categoria, precio = producto
        if termino_busqueda in nombre.lower():
            resultados.append(producto)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} producto(s) que coinciden con '{termino_busqueda}':")
        print(f"{'No.':<4} {'Nombre':<20} {'Categoría':<15} {'Precio':<10}")
        print("-" * 55)
        
        for i, producto in enumerate(resultados, 1):
            nombre, categoria, precio = producto
            print(f"{i:<4} {nombre:<20} {categoria:<15} ${precio:<9}")
    else:
        print(f"No se encontraron productos que coincidan con '{termino_busqueda}'.")

def eliminar_producto(productos):
    """Elimina un producto de la lista por su posición"""
    print("\n--- ELIMINAR PRODUCTO ---")
    
    if not productos:
        print("No hay productos registrados para eliminar.")
        return
    
    mostrar_productos(productos)
    
    while True:
        try:
            numero = int(input(f"\nIngrese el número del producto a eliminar (1-{len(productos)}): "))
            if 1 <= numero <= len(productos):
                producto_eliminado = productos.pop(numero - 1)
                print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.")
                break
            else:
                print(f"Error: Ingrese un número entre 1 y {len(productos)}.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def main():
    """Función principal del programa"""
    productos = []  # Lista principal donde se almacenan los productos
    
    print("Bienvenido al Sistema de Gestión Básica de Productos")
    
    while True:
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("\n¡Gracias por usar el Sistema de Gestión Básica de Productos!")
            print("¡Hasta pronto!")
            break
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()