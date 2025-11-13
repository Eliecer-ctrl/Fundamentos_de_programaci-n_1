def datestr2datetuple(texto):
    dia, mes, año = texto.split('-')
    return dia, mes, año

# Se desarrolla una función que tome como parámetro un texto
# Y devuelve un tupla de tres string que representa la misma fecha