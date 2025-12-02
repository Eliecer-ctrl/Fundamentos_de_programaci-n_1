import re


def d_words(texto):
    patron_diptongo = r'([aáeéoó]h?[iu]|[iu]h?[aáeéoó])'
    texto_min = texto.lower()
    palabras = re.findall(r'[\wáéíóúüñ]+', texto_min)
    final = []
    palabras_unicas = set()
    for palabra in palabras:
        if palabra not in palabras_unicas:
            if re.search(patron_diptongo, palabra):
                final.append(palabra)
                palabras_unicas.add(palabra)
    return final
# Primero se trae al program el módulo re
# ([aáeéoó]h?[iu]|[iu]h?[aáeéoó]) --> vocales fuertes o abiertas, vocales debiles o cerradas 
# El patrón busca una vocal fuerte seguida de una debil o | una vocal debil seguida de una vocal fuerte
# h? --> cero o una vez
# se utilizar re.findall para buscar todas las secuencias que coincide con el patrón






def d_words(texto):
    lista1 = []
    patron = r'([aáeéoó]h?[iu]|[iu]h?[aáeéoó])'
    busqueda = re.findall(patron, texto)
    lista = texto.split()
    for palabra in busqueda:
        if palabra not in lista






