def evaluate(num):
    if type(num) is int:
        return num
    elif type(num) is float:
        return num
    num1, string, num2 = num
    izquierda = evaluate(num1)
    derecha = evaluate(num2)
    if string == '+':
        return izquierda + derecha
    elif string == '-':
        return izquierda - derecha
    elif string == '*':
        return izquierda * derecha
    elif string == '/':
        return izquierda / derecha
# Se toma como parametro una expresion aritmetica simple 
# Puede ser un numero (int o float) o una tupla 
# En el caso dee la tupla se usa recursividad 