from fileparse import parse_csv


#2.18
def leer_camion(nombre_archivo):

    camion = parse_csv(nombre_archivo, types= [str, int, float])
    return camion
  
def leer_precios(nombre_archivo):
    datos = parse_csv(nombre_archivo, has_headers= False)
    diccionario = {}  
    for dato in datos:
        try:
            diccionario[str(dato[0])] = float(dato[1])
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

#informe_camion('../Data/camion.csv', '../Data/precios.csv')