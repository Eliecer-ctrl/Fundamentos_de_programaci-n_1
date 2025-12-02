import re


def normalize(texto):
    st = r'\S+'
    palabras = re.findall(st, texto)
    normal = " ".join(palabras)
    return normal

# Se desarrolla una función que tome como parametro un texto
# Se hace una busqueda exacta de cualquier caracter que no sea un espacio 
