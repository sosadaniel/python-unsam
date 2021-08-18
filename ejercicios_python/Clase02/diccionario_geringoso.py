"""
Ejercicio 2.14: Diccionario geringoso
    Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser las 
    palabras de la lista y los valores deben ser sus traducciones al geringoso (como en el Ejercicio 1.18). Probá tu función para la lista
    ['banana', 'manzana', 'mandarina'].

"""
#2.14
lista = ['banana', 'manzana', 'mandarina']
diccionario = {}
capadepenapa = ''

for elemento in lista:
    for c in elemento:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p'+ c
    diccionario[elemento] = capadepenapa
    capadepenapa = ""

print(diccionario)