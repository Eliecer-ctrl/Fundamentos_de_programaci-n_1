def escala_de_grises(matriz):
    nueva = []
    for fila in matriz:
        fila1 = []
        for rojo, verde, azul in fila:
            media = (rojo + verde + azul) // 3
            fila1.append((media, media, media))
        nueva.append(fila1)
    return nueva