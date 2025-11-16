def chars_frecs(texto1):
    d = {}
    for i in texto1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
# Se desarrolla una función que tome como parametro un texto
# Devuelve un diccionario con la letra y la frecuencia de aparición de la letra 