def fibo_mayor_que(num):
    f1 = 1
    f2 = 1
    if num < 1:
        return 1
    while f2 <= num:
        f1, f2 = f2, f1 + f2
    return f2

# Se desarrolla una funcion que tome como parametro un numero
# Y se calcula la secuencia de fibonacci (suma del los numero anteriores 3 + 5 = 8 + 5 = 13 +8 ...)