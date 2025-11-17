"""




def vecinos_masmedia(nombres):
    if len(nombres) == 1:
        return (None, None)
    else:
        media = longitud_media(nombres)
        vecino = posición(nombres, media)
        final = (nombres[vecino[0]-1], nombres[vecino[0] + 1])
        if vecino[0]-1 == -1:
            resultado = (None, nombres[vecino[0]+1])
        elif vecino[0]+1 > len(nombres)-1:
            resultado = (nombres[vecino[0]-1], None)
        return final





"""