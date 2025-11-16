def format_frecs(data):
    freqs, total_words = data
    result = []
    for word, count in freqs.items():
        frecuencia = (count * 100) / total_words
        formato = f"{word:<10}:{frecuencia:6.2f}%"
        result.append(formato)
    return result
# Se desarrolla una función que tome como parametro una tupla, el 1º valor es un diccionario eel 2º Valor representa el nº total de palabras en el texto
# 1º Desempaqueta la función
# Se calcula la frecuencia
#Formato de Salida (f"{word:<10}:{frecuencia:6.2f}%"): Se utiliza una f-string para construir la cadena final con reglas de formato precisas:
#word:<10: La palabra se alinea a la izquierda (<) dentro de un espacio de 10 caracteres de ancho.
#:: Se añade un separador de dos puntos.
#frecuencia:6.2f: La frecuencia porcentual se formatea con un ancho total de 6 caracteres (6), incluyendo el punto decimal, y se muestra con dos decimales (.2f).
#%: Se añade el símbolo de porcentaje al final