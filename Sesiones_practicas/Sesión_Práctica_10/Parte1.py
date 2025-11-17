def completar_dni(texto):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero_dni = int(texto)
    resto = numero_dni % 23
    letra = letras[resto]
    final = texto + letra
    return final
# Se de sarrolla una función que tome como parametro un texto que representa los numeros de un dni
# Que lo da en forma de string los que se se convierte en un valor de tipo int y se calcula el resto 
# El numero que da es la posición de la letra
# Por último se devuelve el dni con la letra