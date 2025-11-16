def sumar_multiplos(lista1, lista2, num1):
    multiplos = 0
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        if suma % num1 == 0:
            multiplos += suma
    return multiplos
# Se desarrolla una función que tome como parametro dos listas del mismo tamaño y un numero
# Se comprueba que la suma de los elementos de la lista que se encuentre en la misma posicion son multiplos del num1
# Para eso se calcula el resto