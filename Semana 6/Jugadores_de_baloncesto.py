def smallest(lista):
    altura_min = lista[0]
    indice = 0
    for altura in range(1, len(lista)):
        if lista[altura] < altura_min:
            altura_min = lista[altura]
            indice = altura
    return(altura_min, indice)
# Se desarrolla una funcion que tome como parametro una lista de altura 
# Se coge como referencia una altura y luego se compara para acceder al elemento de la lista = lista[altura] y el indice = altura