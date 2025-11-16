def change_sign(lista):
    for numero in range(len(lista)):
        lista[numero] = lista[numero] * -1
    return lista
# Se desarrolla una función que tome como parametro una lista de numeros.
# len --> Devuelve la longitud de la lista  range() --> Crea una secuencia de numeros enteros que comienza desde el 0
# La variable número representa el indice de cada elemento
# el range(len()) puede ser sustituido por el enumerate()
# Devuelve la lista cambiandole el signo a los numeros