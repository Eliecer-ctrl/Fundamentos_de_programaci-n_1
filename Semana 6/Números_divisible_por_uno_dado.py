def divisibles(lista1, numero1):
    cuenta = 0
    for numero in lista1:
        if numero % numero1 == 0:
            cuenta += 1
    return cuenta
# Se desarrolla una función que tome como parametro una lista de nuemros enteros y un número entero.
# Y se devuelve la cuenta de cuantos de los numeros dentro de la lista es divisible por el numero pasado como segundo parametro.