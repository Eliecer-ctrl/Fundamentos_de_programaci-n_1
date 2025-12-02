def save_initials(texto1, texto2):
    with open(texto1, 'r') as file:
        lineas = file.readlines()
    with open(texto2, 'w') as file:
        for linea in lineas:
            palabras = linea.split()
            iniciales_lineas = []
            for palabra in palabras:
                inicial = palabra[0]
                iniciales_lineas.append(inicial)
            resultado = ' '.join(iniciales_lineas)
            file.write(resultado + '\n')
# Se desarrolla una funcion que tome como parametro dos textos 
# El primero en modo letura y el segundo en modo escritura
# Se crea una cadena de palabras con cada linea del texto1
# Se crea una lista y se agrega cada letra inicial de cada pala bra del texto1
# Une los elementos de esa lista en una sola string utilizando un separador 
# Por último se escribe cada letra en el texto2 y con saltos de linea para devolver la misma cantidad de lineas del texto1