# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:47:00 2021

@author: Administrador
"""

def invertir_lista(lista):
    invertida = []
    i = len(lista) 
    
    while i > 0:
        i -= 1
        invertida.append(lista[i])
    
    return invertida