def celsius2fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    c = f"{celsius:5.1f} grados Celsius equivalen a {f:5.1f} grados Fahrenheit"
    return c
# Se desarrolla una función que tome como parametro un numero 
# Se convierte a fahrenheit
# Devuelve una cadena 
# :{5.1f}: Indica que el número debe mostrarse con un ancho total de 5 caracteres (incluyendo el punto decimal y el signo) y un decimal después del punto.