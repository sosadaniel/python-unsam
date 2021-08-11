"""
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión,
 y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
 lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

"""
with open('.\Data/arboles.csv', 'rt') as f:
    costo = 0
    for line in f:
        costo += line[1] * line[2]
    print(costo)