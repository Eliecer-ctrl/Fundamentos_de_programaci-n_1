texto = input("Ingresa un texto: ")
longitud = len(texto)
num1 = int(input(f"Ingresa un número menor que {longitud}: "))

if num1 >= longitud or num1 < 0:
    print(None)
else:
    print("El carácter en la posición", num1, "es:", texto[num1])
# Se pide al usuario que ingrese un texto y un numero positivo que no supere la longitud del texto
# Luego devuelve el caracter que se encuentra en la posición de dicho numero