"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 
de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las 
alturas que alcanza en cada uno de sus primeros diez rebotes.

"""

altura = 100
salto = 0

while salto <=10:
    salto += 1
    altura *= 0.6 
    print(salto, round(altura, 4))
    

