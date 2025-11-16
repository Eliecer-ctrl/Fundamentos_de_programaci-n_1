def add_letter(dni):
    letras = 'TRWAGMYFPDXBMJZSQVHLCKE'
    numero = int(dni)
    letra = letras[numero % 23]
    return dni + letra


def change_dict(dni_dict: dict) -> None:
    for dni in list(dni_dict.keys()):
        nombre = dni_dict[dni]
        dni_con_letra = add_letter(dni)
        dni_dict[dni] = (dni_con_letra, nombre)
# Se tiene un diccionario cuyas claves son strings que representan números de DNI (sin letra) y cuyos valores son nombres de personas. Se quiere modificarlo, manteniendo las claves, pero cambiando los valores de manera que sean tuplas de dos elementos, el primero de los cuales será una string con el número de DNI de la clave, al que se le habrá concatenado la letra, y el segundo, el nombre que era el valor original. Para ello:
# Desarrolle, en el módulo auxiliar, una función llamada add_letter que tome como parámetro una string representando un número de DNI, sin letra, y devuelva el mismo número de DNI al que se le habrá concatenado la letra correspondiente. Para calcular la letra de un DNI, hay que hallar el resto de dividir el número (como entero) entre 23 y usar el valor resultante como índice para seleccionar una letra de la string "TRWAGMYFPDXBNJZSQVHLCKE".
# Desarrolle, en el módulo string_utils, una función llamada change_dict que tome un diccionario como el descrito en el primer párrafo y lo modifique de la forma que allí se describe usando la función desarrollada para el apartado anterior.