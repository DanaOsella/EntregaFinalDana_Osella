# Solicitar al cliente los datos
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
correo = input("Ingrese su correo electrónico:")

# Formatear nombre y apellido (primera letra mayúscula, resto minúscula)
nombre_corregido = nombre.strip().title()
apellido_corregido = apellido.strip().title()

# Eliminar espacios del correo y verificar que tenga solo una "@"
correo_corregido = correo.strip().replace(" ", "")
correo_arroba = correo_corregido.count('@') == 1

# Clasificación por rango etario
if edad < 15:
    categoria_etaria = "Niño/a"
elif 15 <= edad <= 18:
    categoria_etaria = "Adolescente"
else:
    categoria_etaria = "Adulto/a"

# Verificar los requisitos
if (nombre_corregido != "" and
    apellido_corregido != "" and
    correo_corregido != "" and
    correo_arroba and
    edad > 18):
    
    # Mostrar los datos formateados
    print(f"\n--- PRESENTACION CLIENTE ---")
    print(f"Nombre: {nombre_corregido}")
    print(f"Apellido: {apellido_corregido}")
    print(f"Edad: {edad} años - {categoria_etaria}")
    print(f"Correo: {correo_corregido}")
    
else:
    print("\nERROR! Verifique los siguientes puntos:")
    
    if nombre_corregido == "":
        print("- El nombre es obligatorio")
    if apellido_corregido == "":
        print("- El apellido es obligatorio")
    if correo_corregido == "":
        print("- El correo electrónico es obligatorio")
    if not correo_arroba:
        print("- El correo electrónico debe contener exactamente una '@'")
    if edad <= 18:
        print("- Debe ser mayor de 18 años para registrarse")
        print(f"  Actualmente está clasificado como: {categoria_etaria}")