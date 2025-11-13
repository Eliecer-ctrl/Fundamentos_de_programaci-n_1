def vector_sum(vector1, vector2):
    x, y, z = vector1
    x2, y2, z2 = vector2
    sumx = x + x2
    sumy = y + y2
    sumz = z + z2
    return sumx, sumy, sumz
# Se desarrolla una función que tome como parametro dosvectores tridimensionales 
# Y se devuelve las suma de x, y, z