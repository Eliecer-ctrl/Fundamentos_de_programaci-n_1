def progresion(inicial, diferencial, n):
    progres = [inicial]
    for i in range(1, n):
        valo1 = progres[-1]
        valo2 = valo1 + diferencial
        progres.append(valo2)
    return progres
# Se desarrolla un funcion que tome como parametro tres numeros y se calcula la progresion aritmética