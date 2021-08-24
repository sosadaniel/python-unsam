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

#Ejercicio 3.4: Alcances
#Comentario: la función suma no retornaba nada por eso nos daba None como resultado
#Solución: agregué un retun c en la función suma
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#Ejercicio 3.5: Pisando memoria
#Comentario: el problema estaba en que al declarar el diccionario afuera del for lo que hacemos es sobre escribirlo y nunca cambia su valor
#Solucion: Declarar el diccionario como variable local del for, así va retornando un diccionario diferene en cada iteración 
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#3.8

with open('../Data/missing.csv', 'rt' ) as f:
    filas = csv.reader(f)
    encabezado = next(filas)
    for n_fila, fila in enumerate(filas):
        try:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
        except ValueError:
            print(f"La fila {n_fila} No se puede interpretar {fila}")

def leer_camion2(nombre_archivo):

    with open(nombre_archivo, 'rt' ) as f:
        camion= []
        filas = csv.reader(f)
        encabezado = next(filas)
        for n_fila, fila in enumerate(filas):
            try:
                registro= dict(zip(encabezado, fila))
                camion.append(registro)
            except ValueError:
                print(f"La fila {n_fila} No se puede interpretar {fila}")
        return camion

camion2 = leer_camion2('../Data/missing.csv')
pprint(camion2)