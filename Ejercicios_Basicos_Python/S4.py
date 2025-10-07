nombre = "Ana"
producto = "Laptop"
precio = 1200.00
print(f"Hola {nombre}, el producto {producto} cuesta ${precio:.2f}.\n")

nombre_usuario = input("Por favor, ingrese su nombre:\n")
pais_usuario = input("Ahora, si me hace el favor, ingrese el país de residencia:\n")
print(f"Hola, {nombre_usuario} de {pais_usuario}, ¡bienvenido!.\n")

print("Formulario de datos".ljust(10, '-').rjust(10, '-'))
nombre_formulario = input("Por favor, ingrese su nombre:\n")
edad_formulario = input("Si es tan amable, ingrese su edad:\n")
ciudad_formulario = input("De ser posible, ingrese la ciudad en que reside:\n")
print(f"""
    Saludos {nombre_formulario},
    usted está jóven, tan solo tiene {edad_formulario} años,
    y es pistudo porque vive en {ciudad_formulario}.
      """)

base = input("Calcularemos el área de un rectángulo. Por favor, ingrese la base en cm:\n")
altura = input("Ahora, ingrese la altura:\n")
print(f"El área del rectángulo de {base}cmx{altura}cm es de {float(base)*float(altura):.2f}")

print(f"""
|   Producto    |   Precio  |   Cantidad    |   Total   |
---------------------------------------------------------
|   Pan         |   $1.50   |   4           |   $6.00   |
      """)