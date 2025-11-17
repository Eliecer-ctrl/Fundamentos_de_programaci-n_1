def negativo(imagen):
    nueva = []
    for fila in imagen:
        fila1 = []
        for rojo, verde, azul in fila:
            resultado1 = 255 - rojo
            resultado2 = 255 - verde
            resultado3 = 255 - azul
            fila1.append((resultado1, resultado2, resultado3))
        nueva.append(fila1)
    return nueva
