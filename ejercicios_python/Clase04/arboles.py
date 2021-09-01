import csv
import pprint

#Ejercicio 4.15: Lectura de todos los árboles
def leer_parque(nombre_archivo):
    with open(nombre_archivo, encoding= "utf8") as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        arboleda = [dict(zip(encabezado, row)) for row in rows ]
    return arboleda

#Ejercicio 4.17
def altura_diametro(arboleda, especie):
    alt_diam = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return alt_diam

#Ejercicio 4.18: Diccionario con medidas
def medidas_de_especies(especies,arboleda):
    diccionario = {especie: altura_diametro(arboleda, especie) for especie in especies}
    return diccionario



def main():
    arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')
    #Ejercicio 4.16: Lista de altos de Jacarandá
    altura = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    #Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
    altura_d = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    #4.18
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas_de_especies(especies, arboleda)