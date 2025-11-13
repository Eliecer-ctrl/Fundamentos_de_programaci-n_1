def dice_freqs(lista1):
    frecuencia = [0] * 6
    for i in lista1:
        frecuencia[i - 1] += 1
    return frecuencia
# Se desarrolla un función que tome como parametro una lista con la frecuencia de tiradas de un dado y se devuelve una lista con la frecuencia de aparición del 1 al 6