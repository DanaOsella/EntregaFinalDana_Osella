import sqlite3
from colorama import Fore, Style, init

# Inicializar Colorama
init(autoreset=True)

# ================================
#   CONEXIÓN Y CREACIÓN DE TABLA
# ================================

def crear_base():
    """Crea la base de datos y la tabla productos si no existen."""
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)

    conexion.commit()
    conexion.close()


# ================================
#       FUNCIONES DEL CRUD
# ================================

def registrar_producto():
    """Registra un nuevo producto en la base de datos."""
    print(Fore.CYAN + "\n--- REGISTRAR PRODUCTO ---" + Fore.WHITE)

    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break
        except:
            pass
        print(Fore.RED + "Error: ingrese un número entero válido.")

    while True:
        try:
            precio = float(input("Precio: "))
            if precio >= 0:
                break
        except:
            pass
        print(Fore.RED + "Error: ingrese un precio válido.")

    categoria = input("Categoría: ").strip()

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "\nProducto agregado correctamente.")


def mostrar_productos():
    """Muestra todos los productos de la base."""
    print(Fore.CYAN + "\n--- LISTA DE PRODUCTOS ---")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()

    if not productos:
        print(Fore.YELLOW + "No hay productos registrados.")
        return

    print(Fore.MAGENTA + f"{'ID':<5}{'Nombre':<20}{'Cant.':<8}{'Precio':<10}{'Categoría':<15}")
    print(Fore.MAGENTA + "-" * 60)

    for p in productos:
        print(f"{p[0]:<5}{p[1]:<20}{p[3]:<8}{p[4]:<10}{p[5]:<15}")


def buscar_producto_por_id():
    """Busca un producto por su ID."""
    print(Fore.CYAN + "\n--- BUSCAR PRODUCTO POR ID ---")

    try:
        pid = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print(Fore.RED + "ID inválido.")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = cursor.fetchone()

    conexion.close()

    if producto:
        print(Fore.GREEN + "\nProducto encontrado:")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: {producto[4]}")
        print(f"Categoría: {producto[5]}")
    else:
        print(Fore.RED + "No se encontró un producto con ese ID.")


def actualizar_producto():
    """Actualiza los datos de un producto existente."""
    print(Fore.CYAN + "\n--- ACTUALIZAR PRODUCTO ---")

    try:
        pid = int(input("Ingrese el ID a actualizar: "))
    except ValueError:
        print(Fore.RED + "ID inválido.")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = cursor.fetchone()

    if not producto:
        print(Fore.RED + "No existe un producto con ese ID.")
        conexion.close()
        return

    print(Fore.YELLOW + "\nDejar vacío un campo para NO modificarlo.\n")

    nuevo_nombre = input(f"Nombre ({producto[1]}): ").strip() or producto[1]
    nueva_desc = input(f"Descripción ({producto[2]}): ").strip() or producto[2]

    while True:
        nuevo_valor = input(f"Cantidad ({producto[3]}): ").strip()
        if nuevo_valor == "":
            nueva_cant = producto[3]
            break
        try:
            nueva_cant = int(nuevo_valor)
            break
        except:
            print(Fore.RED + "Ingrese un número válido.")

    while True:
        nuevo_precio = input(f"Precio ({producto[4]}): ").strip()
        if nuevo_precio == "":
            nuevo_precio = producto[4]
            break
        try:
            nuevo_precio = float(nuevo_precio)
            break
        except:
            print(Fore.RED + "Ingrese un número válido.")

    nueva_cat = input(f"Categoría ({producto[5]}): ").strip() or producto[5]

    cursor.execute("""
        UPDATE productos
        SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=?
        WHERE id=?
    """, (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_cat, pid))

    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto actualizado correctamente.")


def eliminar_producto():
    """Elimina un producto usando su ID."""
    print(Fore.CYAN + "\n--- ELIMINAR PRODUCTO ---")

    try:
        pid = int(input("Ingrese el ID a eliminar: "))
    except:
        print(Fore.RED + "ID inválido.")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = cursor.fetchone()

    if not producto:
        print(Fore.RED + "No existe un producto con ese ID.")
        conexion.close()
        return

    cursor.execute("DELETE FROM productos WHERE id = ?", (pid,))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto eliminado correctamente.")


def reporte_stock_bajo():
    """Muestra productos con cantidad igual o inferior al límite indicado."""
    print(Fore.CYAN + "\n--- REPORTE DE STOCK BAJO ---")

    try:
        limite = int(input("Mostrar productos con cantidad <= "))
    except:
        print(Fore.RED + "Valor inválido.")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    conexion.close()

    if not productos:
        print(Fore.YELLOW + "No hay productos con stock bajo.")
        return

    print(Fore.MAGENTA + f"\nProductos con cantidad <= {limite}")
    print(Fore.MAGENTA + f"{'ID':<5}{'Nombre':<20}{'Cant.':<8}{'Precio':<10}{'Categoría':<15}")
    print(Fore.MAGENTA + "-" * 60)

    for p in productos:
        print(f"{p[0]:<5}{p[1]:<20}{p[3]:<8}{p[4]:<10}{p[5]:<15}")


# ================================
#           MENÚ PRINCIPAL
# ================================

def mostrar_menu():
    print(Fore.BLUE + "\n" + "="*45)
    print(Fore.BLUE + "      SISTEMA DE GESTIÓN DE INVENTARIO")
    print(Fore.BLUE + "="*45)
    print(Fore.CYAN + "1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock bajo")
    print("7. Salir")
    print(Fore.BLUE + "="*45 + Style.RESET_ALL)


def main():
    crear_base()

    while True:
        mostrar_menu()
        opcion = input(Fore.GREEN + "Seleccione una opción: ").strip()

        match opcion:
            case "1": registrar_producto()
            case "2": mostrar_productos()
            case "3": buscar_producto_por_id()
            case "4": actualizar_producto()
            case "5": eliminar_producto()
            case "6": reporte_stock_bajo()
            case "7":
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                break
            case _:
                print(Fore.RED + "Opción inválida. Intente nuevamente.")

        input(Fore.YELLOW + "\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()
