def swap(texto):
    cadena = texto.split()
    cadena.reverse()
    for palabra in range(len(cadena)):
        cadena[palabra] = cadena[palabra].tittle()
    testo2 = " ".join(cadena)
    return testo2
# Se desarrolla una función que tome como parametro un texto
# 1º Conviente el texto en una cadena [][][][] y lo revierte
# 2º Pone la primera letra de cala palabra de la cadena en mayuscula y las demás en minusculas
# 3º Devuelve el texto