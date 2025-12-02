import re


def verbs(texto):
    lista = []
    conjugada = r'\b(\w*o|\w*a|\w*as|\w*amos|\w*áis|\w*an)\b'
    busqueda = re.finditer(conjugada, texto)
    for elemento in busqueda:
        lista.append(elemento.group())
    return lista

# Para usar expreciones regulares primero se importa re
# se crea una variable verbo a la que se le va a asignar una string raw( que significa sin procesar) que simplifica el manejo de los \
# El proposito de este es bucar cualquier palabra que termine de dicha forma
#\b: limite de la palabra  (): grupo de captura  \w* : raíz del verbo
# |: operador or lo que permite que coincida con cualquiera de las seis terminaciones
# re.finditer() --> busca todas las coincidencias dentro del texto
#match.group() --> recupera el texto que fue capturado por el primer grupo de captura es decir en ()