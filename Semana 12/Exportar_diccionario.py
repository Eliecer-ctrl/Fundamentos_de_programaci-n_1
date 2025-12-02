def export_dict(diccionario, texto):
    with open(texto, 'w') as file:
        for key, tupla in diccionario.items():
            elemento = [key]
            for numero in tupla:
                valor = str(numero)
                elemento.append(valor)
            linea_nueva = ','.join(elemento)
            file.write(linea_nueva + '\n')