import random


#5.1
def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(0,6))
    return tirada

def es_generala(tirada):
    generala = True 
    dado = tirada[0]
    for e in tirada:
        if e != dado:
            generala = False
    return generala

#5.2
def prob_generala(N):
    generala = 0
    for i in range(N):
        for j in range(3):
            tirada = tirar()
            if es_generala(tirada) == True:
               generala += 1
               break
    resultado = generala / N 
    print(generala)
    return resultado

#5.3
def cocumple(n):
    cumples = []
    for i in range(30):  
        cumples.append(random.randint(0,365))      
    print(cumples)

def repite_cumple(cumples):
    for cumple in cumples:
        print()
    
    return None


def main():
    
    print(cocumple(10000))

main()

