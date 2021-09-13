
#Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    i = len(lista) 
    while i > 0:
        i -= 1
        invertida.append(lista[i])
    return invertida
