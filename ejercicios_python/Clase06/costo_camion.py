from informe_funciones import leer_camion

#2.9
def costo_camion(nombre_archivo):
    datos = leer_camion(nombre_archivo)
    costo_total = 0

    for i, e in enumerate(datos, start=1):
        try:
            ncajones = e['cajones']
            precio =  e['precio']
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {i}: No pude interpretar')

    return costo_total




