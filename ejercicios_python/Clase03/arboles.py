"""
Ejercicio 3.18: Lectura de los árboles de un parque
    Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del csv es un árbol).
"""
import csv
from collections import Counter

#3.18
def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, encoding= "utf8") as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        lista = []
        for row in rows:
            if row[10] == parque:
                diccionario = dict(zip(encabezado, row))
                lista.append(diccionario)
    return lista
#3.19
def especies(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    unicos = set(lista)
    return unicos

#3.20
def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        contador[arbol['nombre_com']] += 1
    tendencia = contador.most_common(5)
    return tendencia

#3.21
def obtener_alturas(lista_arboles, especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(float(arbol['altura_tot']))
    altura_prom = sum(lista) / len(lista)
    print(f"La altura maxima es: {max(lista)}\nLa altura promedio es: {round(altura_prom, 2)}")
        
    return lista
#3.22
def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(float(arbol['inclinacio']))
    
    return lista

#3.23
def especimen_mas_inclinado(lista_arboles):
    maxima_inclinacion = 0
    resultado = ""
    especies_v = especies(lista_arboles)
    for especie in especies_v:
        lista = obtener_inclinaciones(lista_arboles, especie)
        maximo = max(lista)
        if maximo > maxima_inclinacion:
            resultado = f"El arbol de especie: {especie} tiene la mayor incliancion con unos {maximo} grados"
            maxima_inclinacion = maximo
    print(resultado)

#3.24
def especie_promedio_mas_inclinada(lista_arboles):
    promedio_maximo = 0
    resultado = ""
    especies_v = especies(lista_arboles)
    for especie in especies_v:
        lista = obtener_inclinaciones(lista_arboles, especie)
        promedio = sum(lista) / len(lista)
        if promedio > promedio_maximo:
            resultado = f"El arbol de especie: {especie} tiene el mayor promedio de incliancion con {promedio} grados"
            promedio_maximo = promedio
    print(resultado)
    

arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "ANDES, LOS")
especies_arboles = especies(arboles)
contador = contar_ejemplares(arboles)
alturas = obtener_alturas(arboles, "Jacarandá")
inclinacion = obtener_inclinaciones(arboles, "Jacarandá")
especie_promedio_mas_inclinada(arboles)

