def delete_value(lista, num):
    while num in lista:
        lista.remove(num)
# Se desarrolla una función que tome como parametro una lista de numero enteros y un numero.
# Se elimina todas las ocurrencias del numero pasado como segundo parametro dentro de la lista

# 2º Forma

def delete_value_for_new(lista, num1):
    # Creamos una lista vacía para almacenar los elementos que queremos conservar
    nueva_lista = []
    
    # Iteramos sobre cada elemento (valor) de la lista original
    for elemento in lista:
        # Si el elemento NO es el valor que queremos eliminar (num1)...
        if elemento != num1:
            # ... lo añadimos a la nueva lista.
            nueva_lista.append(elemento)
            
    # Devolvemos la nueva lista sin las ocurrencias de num1
    return nueva_lista