def symmetrical(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i][j] != lista[j][i]:
                return False
    return True
# Se desarrolla una función que tome como parametro una lista de listas que representa una matriz
# Se comprueba si es simétrica 