nom = input("Por favor, ingrese su nombre a continuación:\n")
print(f"Saludos {nom}.\n")

edad = input("Por favor, ingrese su edad:\n")
print(f"El doble de su edad es de {int(edad)*2} años. Usted está joven.\n")

num1 = input("Por favor, ingrese un número entero a continuación:\n")
num2 = input("Ingrese un segundo número entero:\n")
print(f"El resultado de la suma entre el primer y segundo número es: {int(num1) + int(num2)}.\n")

decimal = input("Por favor, ingrese un número decimal:\n")
print(f"La mitad del decimal ingresado es: {float(decimal)/2}.\n")

anio_nacimiento = input("Por favor, ingrese el año en que nació:\n")
print(f"Usted tiene {2025-int(anio_nacimiento)} años de edad.\n")

precio_producto = input("Por favor, ingrese el precio de un producto:\n")
cantidad_unidades = input("Ahora, si es tan amable, ingrese la cantidad de unidades del producto:\n")
print(f"El total a pagar es de ${float(precio_producto)*float(cantidad_unidades)}.\n")

num = input("Por favor, ingrese un número entero:\n")
print(f"El cuadrado del número entero ingresado es {int(num)*int(num)}.\n")

num01 = input("Por favor, ingrese el primer número para calcular un promedio:\n")
num02 = input("Ahora, de ser posible, ingrese el segundo número:\n")
print(f"El promedio entre {num01} y {num02} es {(float(num01)+float(num02))/2}.\n")

nombre_completo = input("Por favor, ingrese su nombre completo:\n")
edad_usuario = input("Ahora, si es usted tan amable, ingrese su edad:\n")
print(f"Hola, {nombre_completo}. Usted tiene {edad_usuario} años.\n")