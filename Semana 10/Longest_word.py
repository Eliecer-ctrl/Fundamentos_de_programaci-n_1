def longest_word(texto):
    palabras = texto.split()
    larga = ""
    cadena = 0
    for palabra in palabras:
        if len(palabra) > cadena:
            cadena = len(palabra)
            larga = palabra
    return larga
# Se desarrolla una función que tome como parametro un texto
# Convierte el texto en una cadena y se comprueba cual es la palabra más larga
# Y la devuelve