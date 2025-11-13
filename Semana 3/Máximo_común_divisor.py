def mcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# Se desarrolla la funcion que tome como parametro dos nº
# Mientras que el num2 sea distinto de 0
# num1 = num2 y num2 = num1 % num2
# Devuelve el maximo común divisor