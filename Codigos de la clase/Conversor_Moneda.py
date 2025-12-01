print("===Presentación del Cliente===")
nombre = input("Ingresa tu Nombre:")
apellido = input("Ingresa tu Apellido:")
cant_pesos = float(input("Ingrese la cantidad de pesos:"))
edad = int(input("Ingrese su edad:"))
correo = input("Ingresa tu Correo:")

usd = 900
eur = 950

monto_usd = cant_pesos / usd
monto_eur = cant_pesos / eur

ancho = 40
titulo = "Tarjeta de Presentación"
linea_titulo = f"║ {titulo.center(ancho - 4)} ║"

linea_nombre = f"║ Nombre: {nombre} {apellido}".ljust(ancho - 1) + "║"
linea_edad = f"║ Edad: {edad}".ljust(ancho - 1) + "║"
linea_correo = f"║ Correo: {correo}".ljust(ancho - 1) + "║"
linea_cliente = "║ Cliente: ${nombre}".ljust(ancho - 1) + "║"
linea_ars = f"║ Monto en ARS: ${cant_pesos}".ljust(ancho - 1) + "║"
linea_usd = f"║ En USD: ${round(monto_usd, 2)}".ljust(ancho - 1) + "║"
linea_eur = f"║ En USD: ${round(monto_eur, 2)}".ljust(ancho - 1) + "║"

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
{linea_ars}
{linea_usd}
{linea_eur}
{borde_inferior}
"""
print("\n¡Registro completado! Aquí está la tarjeta del cliente:\n")
print(tarjeta)