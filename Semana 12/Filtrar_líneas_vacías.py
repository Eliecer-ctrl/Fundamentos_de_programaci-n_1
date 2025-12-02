def no_empty_lines(texto1, texto2):
    with open(texto1, 'r') as file:
        linias = file.readlines()
    with open(texto2, 'w') as file:
        for linia in linias:
            if linia.strip():
                file.write(linia)
# Se desarrolla una función que tome como parametro dos textos
# Se usa el metodo with para abrir el archivo y se cierre automaticamente después de habrlo utilizado
# Se abre el archivo en modo lectura  ('r') siguinedo simpre la misma estructura
# Se utiliza la funcion readline para leer una linea cada vez que se le llama
# Se abre el segundo texto en modo escritura siempre siguiendo la misma estructura
# Se crea un bucle para leer linea por linea del texto1 y se usa la función strip() para eliminar los caracteres espaciadores 
# Por último se escribe esas lineas sin espacios en el texto2