import random 
import numpy as np
import matplotlib.pyplot as plt


#5.10
def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

#5.11
def album_incompleto(A):
    incompleto = False
    if 0 in A:
        incompleto = True
    return incompleto

#5.12
def comprar_figu(figus_total):
    figurita = random.randint(0, figus_total - 1)
    return figurita

#5.13
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    contador = 0
    while album_incompleto(album) == True:
        contador += 1
        figurita = comprar_figu(figus_total)
        if album[figurita] == 0:
            album[figurita] = 1

    return contador
    
#5.15
def experimento_figus(n_repeticiones, figus_total):
    lista = []
    for i in range(n_repeticiones):
        lista.append(cuantas_figus(figus_total))
        
    return np.mean(lista)

#5.17
def comprar_paquete(figus_total, figus_paquete):
    figuritas = []
    for i in range(figus_paquete):
        figurita = random.randint(0, figus_total - 1)
        figuritas.append(figurita)
    return figuritas

#5.18
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    contador = 0
    while album_incompleto(album) == True:
        contador += 1
        figuritas = comprar_paquete(figus_total, figus_paquete)
        for i in range(figus_paquete):
            if album[figuritas[i]] == 0:
                album[figuritas] = 1

    return contador
#5.21
def plotear_figuritas(figuritas):
    plt.hist(figuritas, bins = 10)
    plt.show()
    return None


def main():
    
    #5.14
    """n_repeticiones = 100
    lista = []
    for i in range(n_repeticiones):
        lista.append(cuantas_figus(670))
        
    resultado = np.mean(lista)
    print(resultado)"""
    
    #5.19
    """n_repeticiones = 100
    lista = []
    for i in range(n_repeticiones):
        lista.append(cuantos_paquetes(670, 5))
        
    resultado = np.mean(lista)
    print(resultado)"""

    #5.20
    n_repeticiones = 100
    lista = []
    for i in range(n_repeticiones):
        lista.append(cuantos_paquetes(670, 5))
    n_paquetes = np.array(lista)
    arreglo = (n_paquetes <= 850).sum()
    resultado2 = (arreglo * 100 )/ n_repeticiones
        
    resultado = np.mean(lista)
    print(f"Para completar el album se necesitan en promedio: {resultado} paquetes")
    print(f"La probabilidad de que completemos el album con 850 paquetes o menos es de {resultado2}%")

    plotear_figuritas(n_paquetes)
    
