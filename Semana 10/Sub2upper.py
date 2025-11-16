def sub2upper(texto1, texto2):
    mayusculas = texto2.upper()
    texto3 = texto1.replace(texto2, mayusculas)
    return texto3
# Se desarrolla dos funciones que tome como parametro dos textos
# Se covierte las palabras del texto2 en mayusculas
# Se remplaza las palabras del texto1 que coincida con las palabras del texto2 por las palabras del texto2 en mayusculas
# Devuelve un nuevo texto
# El primer argumento (texto2) es el patrón que se busca.
# El segundo argumento (mayusculas) es la cadena que se usará para reemplazar el patrón.