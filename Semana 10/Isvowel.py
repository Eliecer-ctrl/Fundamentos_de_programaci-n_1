def isvowel(texto):
    vocales = "aeiouüáéíóúAEIOUÜÁÉÍÓÚ"
    for letras in texto:
        if letras not in vocales:
            return False
    return True
# Se desarrolla una función que tome como parametro un texto
# Y devuelve true si solo el texto está compuesto por vocales