
#Ejercicio 4.6: Propagación
def propagar(lista):
    fin = len(lista) - 1
    queda = True
    while queda != False:
        for i, e in enumerate(lista):
                if i > 0 and i < fin:
                    anterior = lista[i-1]
                    siguiente = lista[i+1]
                    if e == 0 and (anterior == 1 or siguiente == 1):
                        lista[i] = 1
                    elif e == 1: 
                        if anterior == 0:
                            lista[i-1] = 1
                        if siguiente == 0:
                            lista[i+1] = 1
        queda = check_f(lista)
    return lista
def check_f(lista):
    queda = False
    fin = len(lista) - 1
    for i, e in enumerate(lista):
            if i > 0 and i < fin:
                anterior = lista[i-1]
                siguiente = lista[i+1]
                if e == 0 and (anterior == 1 or siguiente == 1):
                    queda = True
                elif e == 1 and (anterior == 0 or siguiente == 0):
                    queda = True
    return queda

def main():
    l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    l2 = [ 0, 0, 0, 1, 0, 0]
    print(propagar(l2))