"""
Ejercicio 3.17: Tablas de multiplicar
    E scribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9
    usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

"""
encabezado = tuple(range(0,10))
print('  %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d\n' % encabezado)
print(("-------------") *5, "\n")
for filas in range(0,10):
    num = 0
    tabla = ""
    for columnas in range(0,10):
        tabla += f"{num:>5d} "
        num += filas 
    print(f"{filas}:{tabla:>5s} ")
    print('\n')
    


