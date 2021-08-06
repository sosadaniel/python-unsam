"""
Ejercicio 1.18: Geringoso rústico
    Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu'
    según corresponda luego de cada vocal.

"""
cadena = 'geringoso'
capadepenapa = ''

for c in cadena:
    capadepenapa += c
    if c == 'a':
        capadepenapa += 'pa'
    elif c == 'e':
        capadepenapa += 'pe'
    elif c == 'i':
        capadepenapa += 'pi'
    elif c == 'o':
        capadepenapa += 'po'
    elif c == 'u':
        capadepenapa += 'pu'

print(capadepenapa)