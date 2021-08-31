



def buscar_n_elemento(lista, e):
    contador = 0
    for elemento in lista:
        if elemento == e:
            contador += 1
    return contador

def maximo(lista):
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m

