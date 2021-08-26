"""
Ejercicio 3.9: La función zip()
    Modificá el programa informe.py que escribiste antes (ver Ejercicio 2.18) para que use esta técnica para elegir las columnas a partir de sus encabezados.

"""
import csv

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        row = csv.reader(f) 
        encabezado = next(row)
        camion = []
        for line in row:
            record = dict(zip(encabezado, line))
            camion.append(record)
        print(camion)
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

compra = leer_camion("../Data/fecha_camion.csv")
venta = leer_precios('../Data/precios.csv')
costo_camion = 0
ganancia_ventas = 0
for producto in compra:
    if producto['nombre'] in venta:
        costo = int(producto['cajones'])  * float(producto['precio'])
        ganancia = venta[producto['nombre']] * int(producto['cajones']) 
        renta = ganancia - costo
        costo_camion += costo
        ganancia_ventas += ganancia

print(f"El costo del camion fue: {costo_camion} \nLo recaudado fue de: {ganancia_ventas} \nDiferencia: {ganancia_ventas- costo_camion}" ) 