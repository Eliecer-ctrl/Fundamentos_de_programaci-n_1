def format_pows(num1):
    if not (0 <= num1 <= 9):
        raise ValueError

    cuadrado = num1 ** 2
    cubo = num1 ** 3
    formato = f"{num1:02}"
    formato1 = f"{cuadrado:3}"
    formato2 = f"{cubo:$>4}"
    return f"{formato}{formato1}{formato2}"
# Se desarrolla una función que tome como parametro un numero
# Si el numero no se encuentra en el rango del 0 al 9 devuelve error
# num1:02: Este es un formato de número de dos caracteres de ancho (2), con relleno de cero (0)
# cuadrado:3: Este es un formato de número con un ancho total de tres caracteres (3).
#cubo:$>4: Este es el formato más complejo:
#4: El ancho total de la cadena debe ser de cuatro caracteres.
#>: Indica que el número debe alinearse a la derecha.
#$: Es el carácter de relleno.
#Ejemplo: Si cubo es 125 (de 53), el resultado es "$125" (signo de dólar, 1, 2, 5).