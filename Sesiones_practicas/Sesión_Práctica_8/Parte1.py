def mcd(num1, num2):
    if num2 == 0:
        return num1
    resto = num1 % num2
    resultado = mcd(num2, resto)
    return resultado
# Se desarrolla una función que tome como parametro dos numeros 
# Caso base si el num2 == 0 devuelve el num1
# Se calcula el máximo común divisor usando recursividad

# Repaso
def mcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        resto = num1 % num2
        llamar = mcd(num2, resto)
    return llamar