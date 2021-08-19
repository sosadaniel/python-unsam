#Ejercicio 3.1: Semántica
"""
Comentario: El error de este program era que solo iteraba una sola vez ya que estaba mal pocionado el return y nunca
aumentaba el valor de i además de no tener en cuenta la mayuculas.
Cambios: se cambio la posición del return False y se agregó la acéptación de mayuculas quitando el == y agregando un "in"

 """
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'Aáa':
            return True
        i += 1
        
    return False
    

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#Ejercicio 3.2: Sintaxis
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Ejercicio 3.3: Tipos
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            print("si", i)
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)