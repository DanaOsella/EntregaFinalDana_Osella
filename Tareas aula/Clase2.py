print("===Presentación del Cliente===")
nombre = input("Ingresa tu Nombre:")
apellido = input("Ingresa tu Apellido:")
edad = int(input("Ingrese su edad:"))
correo = input("Ingresa tu Correo:")

ancho = 40
titulo = "Tarjeta de Presentación"
linea_titulo = f"║ {titulo.center(ancho - 4)} ║"

linea_nombre = f"║ Nombre y Apellido: {nombre} {apellido}".ljust(ancho - 1) + "║"
linea_edad = f"║ Edad: {edad}".ljust(ancho - 1) + "║"
linea_correo = f"║ Correo: {correo}".ljust(ancho - 1) + "║"
linea_cliente = "║ Cliente: ${nombre}".ljust(ancho - 1) + "║"

borde_superior = "╔" + "═" * (ancho - 2) + "╗"
separador = "╠" + "═" * (ancho - 2) + "╣"
borde_inferior = "╚" + "═" * (ancho - 2) + "╝"

tarjeta = f"""
{borde_superior}
{linea_titulo}
{separador}
{linea_nombre}
{linea_edad}
{linea_correo}
{borde_inferior}
"""
print("\n¡Registro completado! Aquí está la tarjeta del cliente:\n")
print(tarjeta)