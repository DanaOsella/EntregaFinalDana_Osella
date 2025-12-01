# Solicitar al cliente los datos
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
correo = input("Ingrese su correo electrónico:")

# Verificar los requisitos
if (nombre.strip() != "" and
    apellido.strip() != "" and
    correo.strip() != "" and
    edad > 18):
    # Mostrar los datos
    print(f"{nombre}\n{apellido}\n{edad}\n{correo}")
else:
    print("ERROR!")

