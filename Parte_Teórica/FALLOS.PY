z = 0
i = 0
while i < 3:
    for j in range(2):
        z += i + j
    i += 1
# Desarrollo: z comienza en 1 z = 1 luego 2, 4, 6 y 9

x = 0
i = 1
while i < 6:
    x += i
    i += 2
# Desarrollo: 1, 3     3, 5    5, 7

x = 1
y = 0
i = 1
while i <= 3:
    x *= i
    y += x
    i += 1
print(y)
# Desarrollo: 1, 1, 2      2, 3, 3      6, 9, 4   

x = 0
for i in range(3):
    j = 0
    while j < i:
        x += 1
        j += 1
# Desarrollo: Se ejecuta 2 veces. x es 3
z = 0
for i in range(4):
    z += i * i
    # Desarrollo: 14



tupla1 = (12, 16, 22, 26, 32, 36, 42, 46)
tupla2 = tupla1[1:-1]
# Solución: recorre desde 16 al 42


x = 1
y = 0
nums = [1, 2, 3, 4]
for num in nums:
    x *= num
    y += x
print(y)
# Solución: 1 +2 +6 +24 == 33

x = 0
nums = [2, 4, 6, 8, 10]
for num in nums:
    x += num // 2
print(x)
# Solución:  1 + 2 + 3 + 4 + 5 = 15



suma = 0
valores = [[1, 2], [3, 4], [5]]
for sub in valores:
    suma += sub[-1]
print(suma)

# Solución: 11 porque va accediendo al ultmo elemento de cada sublista


x = 0
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 != 0:
        x += num
print(x)
# Solución: 9

z = 0
nums = [1, 2, 3, 4]
for num in nums:
    z += num ** 2
# Resultado = 1 + 4 + 9 + 16 = 30



x = 0
nums = [5, 10, 15, 20, 30]
for num in nums:
    if num % 10 == 0:
        x += num
print(x)
# Resultado: 60 



a = [5, 7, 9]
b = [5, 7, 2, 6]
# Solución: La lista a es más grande porque los elementos dentro de la lista a es más grande que los elementos dentro de la lista b.




def func(s):
    if len(s) == 0:
        return 0
    else:
        if type(s[-1]) == int:
            return func(s[0:-1]) + s[-1]
        else:
            return func(s[0:-1])
# Resultado: Si el último elemento de la lista es de tipo int, suma los elementos en el rango + el último elemento 



# si a = 8 y b = 15 ¿Qué resultado devuelve la siguiente función?

def func(a, b):
    if a == 0:
        return 0
    if a % 2 != 0:
        return func(a // 2, b * 2)
    return func(a // 2, b * 2)
#Solución: (4, 30) (2, 60) (0, 120) (0)


#si a = 8 y b = 15 ¿Qué resultado devuelve la siguiente función?

def func(a, b):
    if a == 0:
        return 0
    if a % 2 != 0:
        return b + func(a // 2, b * 2)
    return func(a // 2, b * 2)
# Resultado: 120

# si s = [0, 2, 1, 3, 0, -4, 5] ¿Qué resultado devuelve la siguiente función?

def func(s):
    a = (0, 0)
    if len(s) > 0:
        a = func(s[1:])
        if s[0] > 0:
            a =  (1 + a[0], a[1])
        else:
            a = (a[0], 1 + a[1])
    return a

#Solución: a = (0,0) --> (0,1) (1, 1) (2, 1) (3, 1) (3, 2) (3, 3) (4, 3)



x = True
y = True
z = False

print(not x and (y or not z and True))
# Solucion: False --> and --> 2true or --> 1true



y = 1
for i in range(4):
    y *= i
    i += 1
# Solución: 0


x = 0
y = 1
i = 0
while i < 4:
    x += y
    y *= 2
    i += 1
print(x)
# x = 1 y = 2  x = 3 y = 4 x = 7 y = 8 x = 15 y = 16





































