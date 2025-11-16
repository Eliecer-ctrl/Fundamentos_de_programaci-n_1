def get_values(d, lista):
    nueva = []
    for elemento in lista:
        nueva.append(d.get(elemento))
    return nueva
# Se desarrolla una nueva función qque tome como parametro un diccionario y una lista de claves
# Devuelve una nueva lista con los valores de dichas claves que aparecen en el diccionario
# El d.get() solo se usa para acceder a las claves y comprobar si la clave de la lista está en diccionario 
# Si no se encuentra la clave devuelve None