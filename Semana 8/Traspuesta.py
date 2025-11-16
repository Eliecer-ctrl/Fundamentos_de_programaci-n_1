def transpose(lista1):
    filas = len(lista1)
    columnas = len(lista1[0])
    traspuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            traspuesta[j][i] = lista1[i][j]
    return traspuesta
# Se desarrolla una funcion que tome com parametro una lista de lista
# Devuelve la matríz traspuesta
def transpose(lista1):
    filas = len(lista1)          # Dimensión i de la matriz original
    columnas = len(lista1[0])    # Dimensión j de la matriz original
    
    # 1. Creación de la Matriz Traspuesta (Inicializada con ceros)
    # Crea una matriz de 'columnas' filas y 'filas' columnas.
    traspuesta = []
    # El bucle exterior crea las filas de la nueva matriz (que son 'columnas' filas)
    for _ in range(columnas):
        nueva_fila = []
        # El bucle interior crea las columnas de la nueva matriz (que son 'filas' columnas)
        for _ in range(filas):
            nueva_fila.append(0)
        traspuesta.append(nueva_fila)
    
    # --- Asignación de Elementos ---

    # 2. Bucle para Recorrer las Filas de la Matriz Original (índice i)
    for i in range(filas):
        
        # 3. Bucle para Recorrer las Columnas de la Matriz Original (índice j)
        for j in range(columnas):
            
            # 4. La Regla de Transposición: Inversión de Índices
            # El elemento en la posición (i, j) de la original va a la posición (j, i) de la traspuesta.
            traspuesta[j][i] = lista1[i][j]
            
    return traspuesta