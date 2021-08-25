"""
Ejercicio 3.18: Lectura de los árboles de un parque
    Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del csv es un árbol).
"""
import csv
from collections import Counter

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

def especies(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    unicos = set(lista)
    return unicos

def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        contador[arbol['nombre_com']] += 1
    tendencia = dict(contador)
    
    print(contador)

        
        

arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")
especies_arboles = especies(arboles)
contador = contar_ejemplares(arboles)
