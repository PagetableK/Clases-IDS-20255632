a = 10
b = 3
c = 5

print(f"La suma de a y b es {a+b}.")
print(f"El resultado de a dividido entre b es {a/b}.")
print(f"El residuo de dividir a entre c es {a%c}.\n")

numero = 7
print(numero > 5, "\n")

x = 10
y = 10
print(x is y)
print(x is not y)
print("\n")

numero_usuario = input("Por favor, ingrese un número:\n")
print(float(numero_usuario) % 2 == 0 , "\n")

registrado = True
print("and: ", registrado and False)
print("or:", registrado or False)
print("not:", not registrado , "\n")

num1 = input("Por favor, ingrese un número:\n")
num2 = input("Si me puede hacer el favor, ingrese un segundo número:\n")
print("¿El primer número es mayor al segundo número? (num1>num2):", num1>num2,".\n")

edad = input("Por favor, ingrese su edad:\n")
print("¿Usted puede votar? Respuesta:",int(edad)>=18,".\n")

soltero = True
anios_soltero = 19
print(soltero > 18 and soltero, "\n")