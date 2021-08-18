"""
Ejercicio 2.15: Lista de tuplas
    Definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, lo lee y devuelve
    la información como una lista de tuplas.

Ejercicio 2.16: Lista de diccionarios
    Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un 
    diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar
    las diferentes columnas del archivo de entrada.

Ejercicio 2.17: Diccionarios como contenedores
    Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario
    donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.
"""
"""
#2.15
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        next(f)
        camion = []
        for line in f:
            row = line.split(',')
            tupla = (row[0], int(row[1]), float(row[2]))
            camion.append(tupla)
        return camion

camion =leer_camion("./ejercicios_python/Data/camion.csv")
total = 0.0
for nombre, cajones, precio in camion:
    total += cajones * precio
print(total)

#2.16
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        next(f)
        camion = []
        for line in f:
            row = line.split(',')
            diccionario = {
                'nombre' : row[0],
                'cajones' : int(row[1]),
                'precio': float(row[2])
                }
            camion.append(diccionario)
        return camion

camion =leer_camion("./ejercicios_python/Data/camion.csv")
total = 0.0
for s in camion:
    total += s['cajones']*s['precio']
print(total)

#2.17
def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        diccionario = {}
        for line in f:
            row = line.split(',')
            try:
                fruta = row[0]
                precio = float(row[1])
                diccionario[fruta] = precio
            except:
                print("Warning")
    return diccionario

diccionario = leer_precios('./ejercicios_python/Data/precios.csv')
fruta = input("Ingrese la fruta: ")
if fruta in diccionario:
    print(f"El precio de un cajón de {fruta} es: ", diccionario[fruta])
else:
    print(f"{fruta} no figura en el listado de precios.")
"""
#2.18
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        next(f)
        camion = []
        for line in f:
            row = line.split(',')
            diccionario = {
                'nombre' : row[0],
                'cajones' : int(row[1]),
                'precio': float(row[2])
                }
            camion.append(diccionario)
        return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        diccionario = {}
        for line in f:
            row = line.split(',')
            try:
                fruta = row[0]
                precio = float(row[1])
                diccionario[fruta] = precio
            except:
                print("Warning")
    return diccionario

compra = leer_camion("./ejercicios_python/Data/camion.csv")#Lista de diccionario
venta = leer_precios('./ejercicios_python/Data/precios.csv')#Diccionario de precios

for producto in compra:
    if producto['nombre'] in venta:
        renta = (venta[producto['nombre']] * producto['cajones'] ) - (producto['cajones']  * producto['precio'])
        print("Rentabilidad de",producto['nombre'], ": ", round(renta, 2))






   






