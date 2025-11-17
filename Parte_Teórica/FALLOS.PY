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