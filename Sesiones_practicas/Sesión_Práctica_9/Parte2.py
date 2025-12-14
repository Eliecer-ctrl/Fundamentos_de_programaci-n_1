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

def negativo(imagen):
    nueva = []
    for fila in imagen:
        fila2 = []
        for elemento in fila:
            resul = 255 - elemento[0]
            resul1 = 255 - elemento[1]
            resul2 = 255 - elemento[2]
            fila2.append((resul, resul1, resul2))
        nueva.append(fila2)
    return nueva
