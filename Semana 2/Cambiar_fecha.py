fecha1 = input("Introduce la fecha en formato dd-mm-aaaa: ")
dia, mes, año = fecha1.split('-')
nueva_fecha = f'{mes}-{dia}-{año}'
print(nueva_fecha)
# Se introduce una fecha en formato dd-mm-aaaa y se intercambian el mes y el dia usando una cadena.