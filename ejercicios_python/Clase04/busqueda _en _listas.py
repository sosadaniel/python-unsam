#Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista, e):
    contador = 0
    for i, elemento in enumerate(lista):
        if elemento == e:
            contador = i
    return contador

#Ejercicio 4.4: Búsqueda de máximo y mínimo
def maximo(lista):
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m


