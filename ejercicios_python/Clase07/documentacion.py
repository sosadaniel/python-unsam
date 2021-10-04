def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta > desde:
        resultado = desde
        for i in range(desde, hasta ):
            resultado += i+1
            print(resultado)
        sumatoria = sum(range(desde, hasta))
        print('sumatoria: ', sumatoria)
    else:
        resultado = 0
   
    return resultado

def valor_absoluto(n):
    '''
    Pre: recibe un numero cualquiera
    Pos: devuelve su valor absoluto
    '''
    if n >= 0:
        return n
    else:
        return -n
def suma_pares(l):
    '''
    Pre: recibe una lista de numero enteros
    Pos: devuelve la suma de todos los numeros pares que encuentra
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    Pre: recibe dos numero entero
    Pos: devuelve el resultado de su multiplicación
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):

    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
            print('if n = ', n)
        else:
            n = 3 * n + 1
            print('else n = ', n)
        res += 1

    return res

