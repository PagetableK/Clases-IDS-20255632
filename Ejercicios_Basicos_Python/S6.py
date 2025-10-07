frase = "La programación es poderosa"
print("¿La palabra 'poderosa' está dentro de la frase?:",{"poderosa" in frase})
print("¿La palabra 'Java' no se encuentra en la frase?:",{"Java" not in frase})

palabra = "hola"
print(f"La palabra '{palabra}' repetida 5 veces, a continuación:\n{palabra*5}")

texto = "banana"
print(f"En la palabra {texto}, la letra 'a' se repite {texto.count('a')}")

mensaje = "El Salvador es un gran país"
print(f"En el mensaje '{mensaje}', la palabra 'gran' aparece en la posición {mensaje.index("gran")}")