def saludar ():
    print("Hola Mundo")
saludar()

def mostrar_bienvenida(matías):
    print(f"¡Bienvenido/a, {nombre}!")


def calcular_precio_final(precio, impuesto):
    return precio + (precio * impuesto / 100)

def calcular_cuadrado(numero):1
    resultado = numero ** 2
    return resultado

numero_ingresado = int(input("Ingresá un número: "))
cuadrado = calcular_cuadrado(numero_ingresado)
print(f"El cuadrado de {numero_ingresado} es {cuadrado}")


def calcular_area_y_perimetro(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

area, perimetro = calcular_area_y_perimetro(base, altura)
