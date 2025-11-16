def dif_par_impar(lista1, lista2):
    par = 0
    impar = 0
    for numero in range(len(lista1)):
        suma = lista1[numero] + lista2[numero]
        if suma % 2 == 0:
            par += 1
        else:
            impar += 1
    return (par, impar)
# Se desarrolla una función que tome como parametro dos listas
# Y se comprueba que la suma de los elementos de la lista que se encuentra en la misma posición es par o impar