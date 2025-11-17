def longitud_media(nombres):
    total = 0
    for nombre in nombres:
        total += len(nombre)
    media = total / len(nombres)
    return media
# Se desarrolla una funcion que tome como parametros un secuencia de nombres
# Se calcula la media 