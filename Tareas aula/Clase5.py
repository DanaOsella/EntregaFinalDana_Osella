# Pedir datos del cliente
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
cuenta = int(input("Ingrese su número de cuenta: "))

# Formatear nombre y apellido (primera letra mayúscula, resto minúscula)
nombre_corregido = nombre.strip().title()
apellido_corregido = apellido.strip().title()

# Registrar ingresos de 6 meses
mes = 1
total = 0

while mes <= 6:
    ingreso = float(input(f"Ingrese los ingresos del mes {mes}: $"))
    
    if ingreso >= 0:
        total = total + ingreso
        mes = mes + 1
    else:
        print("El valor no es válido, debe ser positivo")

# Calcular promedio
promedio = total / 6

# Mostrar resultados
print(f"\n--- RESUMEN FINANCIERO ---")
print(f"Cliente: {nombre_corregido} {apellido_corregido}")
print(f"Número de cuenta: {cuenta}")
print(f"Total acumulado: ${total}")
print(f"Promedio mensual: ${promedio}")