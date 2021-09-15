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

def imprimir_informe(compra, venta):
    costo_camion = 0
    ganancia_ventas = 0
    for producto in compra:
        if producto['nombre'] in venta:
            costo = producto['cajones']  * producto['precio']
            ganancia = venta[producto['nombre']] * producto['cajones'] 
            renta = ganancia - costo
            costo_camion += costo
            ganancia_ventas += ganancia

    print(f"El costo del camion fue: {costo_camion} \nLo recaudado fue de: {ganancia_ventas} \nDiferencia: {ganancia_ventas- costo_camion}" ) 

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    compra = leer_camion(nombre_archivo_camion)
    venta = leer_precios(nombre_archivo_precios)
    imprimir_informe(compra, venta)

informe_camion('../Data/camion.csv', '../Data/precios.csv')