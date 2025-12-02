def filtrar(imagen, filtro):
    if sum(filtro) != 1 or len(filtro) != 3:
        return
    for i in range(len(imagen)):
        imagen[i] = filtrar_fila(imagen[i], filtro)

def filtrar_fila(fila, filtro):
    nueva = []
    for pixel in fila:
        nuevo_pixel = (
            pixel[0] * filtro[0],
            pixel[1] * filtro[1],
            pixel[2] * filtro[2]
        )
        nueva.append(nuevo_pixel)
    return nueva


def filtrar_sin_auxiliar(imagen, filtro):
    # Lógica de Validación aquí...
    
    # Bucle EXTERNO: Recorre las FILAS (i)
    for i in range(len(imagen)): 
        # Bucle INTERNO: Recorre las COLUMNAS/PÍXELES (j)
        for j in range(len(imagen[i])):
            
            pixel_original = imagen[i][j]
            
            # LÓGICA DE MODIFICACIÓN AQUÍ
            nuevo_pixel = (
                pixel_original[0] * filtro[0],
                pixel_original[1] * filtro[1],
                pixel_original[2] * filtro[2]
            )
            
            # Asignación del nuevo pixel
            imagen[i][j] = nuevo_pixel