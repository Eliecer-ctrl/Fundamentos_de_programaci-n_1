def make_list(tupla, numero):
    nueva = []
    for elemento in tupla:
        resultado = elemento * numero
        nueva.append(resultado)
    return nueva
# Se desarrolla una función que tome como parametro una tupla con valores de tipo float y un numero
# Devuelve una nueva tupla con cada valor de la tupla multiplicado por el numero pasado como segundo parametro 