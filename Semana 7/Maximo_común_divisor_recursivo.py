def mcd(num1, num2):
    if num2 == 0:
        return num1
    r = num1 % num2
    resto = mcd(num2, r)
    return resto
# Se desarrolla una función que tome como parametro dos numeros entero (Maximo comun divisor)
# Se crea el caso base si el num2 == 0 return 1
# Se crea el primer caso y luego se usa recursividad 