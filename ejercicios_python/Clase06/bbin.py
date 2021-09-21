def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio  # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    return pos

def insertar(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    encontrado = False
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio
        if lista[medio] == x:
            pos = medio  # elemento encontrado!
            encontrado = True
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if encontrado == False:
        lista_n = []
        lista_n.extend(lista[:pos])
        lista_n.append(x)
        lista_n.extend(lista[pos:])
        lista = lista_n
    print(lista)
    return pos

