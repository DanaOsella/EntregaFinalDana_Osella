
# contador = 1
# while contador <= 5:
#    print(f"Este es el intento número {contador}.")
#    contador += 1

#    contador = contador + 1  #Es iagual a contador += 1



# nombre = ""

# while nombre == "":
#    nombre = input("Ingresá tu nombre: ").strip() #Strip() elimina espacio vacios antes y desp de la palabra
#    if nombre == "":
#        print("El nombre no puede estar vacío. Intentá de nuevo.")

# print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")


# # Inicializamos el contador en 1
# contador = 1

# # Creamos un bucle que se ejecuta mientras el contador
# # sea menor o igual a 5
# while contador <= 5:
#    # Mostramos el valor actual del contador
#    print(f"Número: {contador}") 

#    # Incrementamos el contador en 1
#    contador += 1 

# # Mensaje final una vez que el bucle termina
# print("Bucle terminado.") 

'''
# Inicializamos el contador en 0
intentos = 0
# Establecemos el máximo de intentos permitidos
max_intentos = 3
# Usamos un bucle que se detendrá si el usuario
# ingresa un nombre válido o si se agotan los intentos
while intentos < max_intentos:
   # Solicitamos al usuario que ingrese su nombre
   nombre = input("Ingresá tu nombre de usuario: ").strip()
'''

'''
intentos = 3

while intentos > 0:
   nombre = input("Ingresá tu nombre de usuario: ").strip()
   if nombre =="":
      intentos -= 1 #este bloque se ejecuta 3 veces
    else:
      break

print("fin")
'''

# intentos = 0
# max_intentos = 3
# mensaje = 3
# nombre = ""
# while intentos < max_intentos and nombre == "":
#    nombre = input("Ingresá tu nombre de usuario: ").strip()
#    if nombre == "":
#        mensaje -= 1
#        print(f"El nombre no puede estar vacío. Te quedan {mensaje} intentos")
#        intentos += 1
# if nombre != "":
#    print(f"Bienvenido/a, {nombre}!")
# else:
#    print("Se agotaron los intentos. Intente más tarde.")

numero = 0
print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.")
suma = 0

while True:
   # Solicitamos al usuario un número
   numero = int(input("Ingresá un número: "))
   # Verificamos si el número es negativo
   if numero < 0:
       print("El número es negativo, se ignora. Intentá de nuevo.")
       continue  
   if numero == 0:
       break
   suma += numero
print(f"La suma de los números positivos es: {suma}")

texto = "  Python  "
print(texto.strip().upper())