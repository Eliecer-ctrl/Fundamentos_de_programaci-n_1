def initials(lista):
    nueva = []
    for fila in lista:
        letra = []
        for nombre in fila:
            letra.append(nombre[0])
        nueva.append(letra)
    return nueva
# Se desarrolla una nueva función que tome como parametro una lista de listas
# Devuelve una nueva lista de listas pero con solo la letra inicial de cada nombre