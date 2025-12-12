# 1
def sumar_longitudes(tupla):
    suma_longitudes = 0
    for elemento in tupla:
        suma_longitudes += len(elementos)
    return suma_longitudes

# 2
def obtener_multiplos_de_tres(tupla):
    multiplos = []
    for numero in tupla:
        if numero % 3 == 0:
            multiplos.append(numero)
    return tuple(multiplos)

#3
def palabra_en_tupla(tupla, palabra):
    if palabra in tupla:
        return True
    else:
        return False

# 4
def palabra_mas_larga(tupla):
    longitud = 0
    for elemento in tupla:
        if len(elemento) > longitud:
            longitud = len(elemento)
    return longitud

# 5
def primer_mayor_que_dado(tupla, num):
    for numero in tupla:
        if numero > num:
            return numero
    return None

# 6
def es_primo(num):
    if num % 3 == 0:
        return True
    else:
        return False

# 7
def contar_vocales(string):
    cuenta = 0
    vocales = "aeiouAEIOU"
    for caracter in string:
        if caracter in vocales:
            cuenta += 1
    return cuenta

# 8 
def indices_primera_vocal(string):
    vocales = "aeiou"
    for i, caracter in enumerate(string):
        if caracter in vocales:
            return i
    return None

# 9

def primer_no_repetido(string):
    frecuencia = {}
    for caracter in string:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    for caracter in cadena:
        if frecuencia[caracter] == 1:
            retrun caracter
    return None



# 10
def contar_caracter(string, caracter):
    contar = 0
    if caracter in string:
        contar += 1

# 11
def juego_adivinar(numero_secreto):
    