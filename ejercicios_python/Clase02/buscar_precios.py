"""
Ejercicio 2.7: Buscar precios
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo
+../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura
en el listado de precios, debe imprimir un mensaje que lo indique.

"""

#2.7
def buscar_precio(fruta):
    existe = False
    with open('./ejercicios_python/Data/precios.csv', 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            if row[0] == fruta:
                print(f"El precio de un cajón de {fruta} es: ", row[1])
                existe = True
        if existe == False:
            print(f"{fruta} no figura en el listado de precios.")

buscar_precio('Kale')

