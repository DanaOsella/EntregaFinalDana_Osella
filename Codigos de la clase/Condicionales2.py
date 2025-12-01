edad = 18
if edad < 18:
    print("Sos Menor")
else:
    nombre = input("Ingrese su nombre:")
    lugar = input("Ingrese su dirección:")
    if nombre == "Matías":
        print("Sos Matías")
    if lugar == "CABA" or lugar == "caba" and edad >= 18:
        print("Sos de CABA")
    print("Sos Mayor")

if temperatura := int(input("Ingrese la temperatura:")) > 30:
    print("Hace calor")

#Match
'''
match variable:
    case valor1:
        #Codigo si variable == valor1
    case valor2:
        #Codigo si variable == valor2
    case _:
        #Si no coincide ningun valor anterior
'''

#Ejemplo Menu (Simple)
print("Elegi una opción: \n1. listar productos \n2. Agregar producto \n3. opcion 3")
opcion = int(input("Ingrese una opción:"))

match opcion:
    case 1:
        print("Mouse,Teclado,Monitor")
    case 2:
        print("CPU,Camara,Parlantes")
    case 3:
        print("Elegiste la opción 3")
    case _:
        print("Opción no valida")


ingreso = 60000

edad = 25

if ingreso < 50000:

    print("Ingresos bajos.")

elif edad < 30:

    print("Joven con buenos ingresos.")

else:

    print("Adulto con buenos ingresos.")


texto = "Python"

if "P" in texto and texto.endswith("on"):

    print("Condición cumplida.")

else:

    print("Condición no cumplida.")
    
match 10:

    case 5:

        print("Cinco.")

    case 10:

        print("Diez.")

    case _:

        print("Otro número.")

dia = input("Ingresá un día de la semana: ")

match dia:

    case "Lunes":

        print("Inicio de semana.")

    case "Viernes":

        print("Fin de semana.")

    case _:

        print("Día intermedio.")