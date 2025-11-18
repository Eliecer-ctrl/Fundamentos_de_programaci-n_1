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
Solución:  1 + 2 + 3 + 4 + 5 = 15



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

































































