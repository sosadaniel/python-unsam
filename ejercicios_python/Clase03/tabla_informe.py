"""
Ejercicio 3.13: Recolectar datos

"""


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

def balances():
    compra = leer_camion("../Data/camion.csv")
    venta = leer_precios('../Data/precios.csv')
    costo_camion = 0
    ganancia_ventas = 0
    for producto in compra:
        if producto['nombre'] in venta:
            costo = producto['cajones']  * producto['precio']
            ganancia = venta[producto['nombre']] * producto['cajones'] 
            costo_camion += costo
            ganancia_ventas += ganancia

    print(f"El costo del camion fue: {costo_camion} \nLo recaudado fue de: {ganancia_ventas} \nDiferencia: {ganancia_ventas- costo_camion:0.2f}" ) 


def hacer_informe(camion, precios):
    lista = []
    for producto in camion:
        if producto['nombre'] in precios:
            ganancia = precios[producto['nombre']] - producto['precio'] 
            tupla = (producto['nombre'], producto['cajones'], producto['precio'], ganancia )
            
            lista.append(tupla)
    return lista


camion = leer_camion("../Data/camion.csv")
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
for r in informe:
    print(r)

#3.14
for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}")

#3.15 
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------\n')
for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}")

#3.16
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------\n')
for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}")
