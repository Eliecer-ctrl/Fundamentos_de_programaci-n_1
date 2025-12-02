def chars_frecs(texto):
    diccionario = dict()
    for elemento in texto:
        if elemento in diccionario:
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1
    return diccionario
# Se desarrolla una función que tome como parametro un texto
# Devuelve un diccionario con la letra y la frecuencia de aparición de la letra 