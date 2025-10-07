palabra = "Python"
print("Primera letra de la palabra 'Python':", palabra[:1:])
print("Tres primeras letras de la palabra 'Python':", palabra[:3])
print("Dos últimas letras de la palabra 'Python':", palabra[4:6],".\n")

frase = "Aprender Python es divertido."
print(frase[frase.index("Python"):frase.index("Python")+6:],"\n")

palabra_usuario = input("Ingrese una palabra cualquiera para encontrar la longitud de caracteres:\n")
print(f"La longitud de la palabra '{palabra_usuario}' es de {len(palabra_usuario)} caracteres.\n")

palabra_input = input("Ingrese una palabra para encontrar la primera y última letra:\n")
print(f"Primera letra de la palabra {palabra_input}: {palabra_input[:1]}.")
print(f"Última letra de la palabra {palabra_input}: {palabra_input[:-2:-1]}.\n")

codigo = "ABC1234XYZ"
print(f"La parte numérica del código '{codigo}' es {codigo[3:7]}.\n")

nombre = "Juan Pérez"
print(f"El apellido de {nombre} es {nombre[5:10]}.")
