"""
Ejercicio 2.2: Lectura de un archivo de datos
    Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión,
    y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
    lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

Ejercicio 2.3: Precio de la naranja
    Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.

Ejercicio 2.6: Transformar un script en una función
    Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) en una función
    costo_camion(nombre_archivo). Esta función recibe un nombre de archivo como entrada, lee la información sobre los
    cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.

"""
#2.2
with open('C:\Projects\python-unsam\ejercicios_python\Clase02\Data\camion.csv', 'rt') as f:
    next(f)
    costo = 0
    for line in f:
        row = line.split(',')
        precio = int(row[1]) * float(row[2])
        costo += precio
    print(costo)

#2.3
with open('C:\Projects\python-unsam\ejercicios_python\Clase02\Data\precios.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        if row[0] == 'Naranja':
            print("El precio de la naranja es: ", row[1] )

#2.6
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        next(f)
        costo = 0
        for line in f:
            row = line.split(',')
            precio = int(row[1]) * float(row[2])
            costo += precio
        return costo

costo =costo_camion('C:\Projects\python-unsam\ejercicios_python\Clase02\Data\camion.csv')
print("Costo total: ", costo)

#2.7
def buscar_precio(fruta):
    with open('C:\Projects\python-unsam\ejercicios_python\Clase02\Data\precios.csv', 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            if row[0] == fruta:
                print(f"El precio de un cajón de {fruta} es: ", row[1] )

buscar_precio('Frambuesa')