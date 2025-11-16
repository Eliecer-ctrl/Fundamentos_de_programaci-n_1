def words_frecs(texto):
    d = {}
    cadena = texto.split()
    for i in cadena:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
# Se desarrolla una función que tome como parametro un texto
# Lo concierte en una cadena [][][] 
# Devuelve un diccionario con las palabras y la frecuencia de aparición