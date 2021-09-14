import random
import numpy as np 

def medir_temp(p):
    mediciones= []
    for i in range(p):
        num = 37.5 + random.normalvariate(0, 0.2)  
        mediciones.append(num)
    np.save('../Data/temperaturas', mediciones)
    return mediciones

def resumen_temp(n):
    promedio = sum(n)/ len(n)
    maximo = max(n)
    minimo = min(n)
    data = sorted(n)
    index = len(data) // 2
    mediana = 0

    if len(n) % 2 == 0:
        mediana = (data[index - 1] + data[index]) / 2
    else:
        mediana = data[index]

    
    return (maximo, minimo, promedio, mediana)

def main(): 
    e =medir_temp(999)