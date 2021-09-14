import csv
import pprint
import matplotlib.pyplot as plt
import numpy as np
import random
np.random.seed(19680801)
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

def scatter_hd(lista_de_pares):
    
    datos = np.array(lista_de_pares)
    altura = [e[0] for e in datos]
    diametro = [e[1] for e in datos]
    N = len(datos)
    colors = np.random.random(N)

    plt.scatter(altura, diametro, alpha=0.5, c=colors)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
    return None



def main():
    arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')
    #Ejercicio 4.16: Lista de altos de Jacarandá
    """altura = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(altura, bins= 20)
    plt.show()"""

    #Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
    altura_d = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    scatter_hd(altura_d)
    #4.18
    #especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    #medidas_de_especies(especies, arboleda)

main()