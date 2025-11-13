def square_root(number, accuracy):
    estimate = number / 2
    while abs(estimate * estimate - number) > accuracy:
        estimate = (estimate + number / estimate) / 2
    return estimate

# Se desarrolla una función que tome como parametro 2 nº
# number = Es el número al que queremos calcular la raíz cuadrada (el radicando)
# accuracy = Es un valor decimal pequeño que define cuán precisa debe ser la respuesta (el margen de error permitido).