def filter_names(lista, letra):
    nueva = []
    for nombre in lista:
        if nombre[0] == letra:
            nueva.append(nombre)
    return nueva
# Se desarrolla una función que toem como parametro una lista y una letra 
# Se comprueba si la letra incial de cada nombre de la lista empieza por la letra pasada como segundo parametro
# Se crea una nueva lista y se agrega en nombre