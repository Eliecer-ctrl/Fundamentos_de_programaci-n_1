def sum_columns(lista1):
    return [sum(columna) for columna in zip(*lista1)]
# Se desarrolla una funcion que tome como parametro una lista de listas 
# Devuelve la suma por columnas
# Ejemplo: Si lista1 = [[1, 2], [3, 4]], entonces *lista1 es equivalente a pasar [1, 2] y [3, 4] como argumentos separados.
def sum_columns_manual(lista1):
    # 1. Determinar las dimensiones
    if not lista1:
        return []
    
    filas = len(lista1)
    columnas = len(lista1[0])
    
    # 2. Inicializar la lista de resultados (una suma por cada columna)
    # Inicialmente, la suma de cada columna es cero.
    sumas_columnas = [0] * columnas
    
    # 3. Iterar y sumar
    
    # El bucle exterior recorre cada fila (i)
    for i in range(filas):
        
        # El bucle interior recorre cada elemento/columna (j)
        for j in range(columnas):
            
            # Sumar el elemento de la fila 'i' y columna 'j' 
            # al total acumulado para esa columna 'j'.
            sumas_columnas[j] += lista1[i][j]
            
    return sumas_columnas