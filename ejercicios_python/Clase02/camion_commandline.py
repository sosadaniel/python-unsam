"""
Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
    Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la 
    lectura de parámetros por línea de comando

"""
import csv, sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        costo = 0
        for row in rows:
            try: 
                precio = int(row[1]) * float(row[2])
                costo += precio
            except ValueError:
                print("Warnig")

        return costo
        
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = './ejercicios_python/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print("Costo total: ", costo)