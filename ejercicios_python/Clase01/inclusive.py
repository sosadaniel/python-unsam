"""
Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra.
Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que 
figuren en el último o anteúltimo caracter de cada palabra por una 'e'. Por ejemplo 'todos somos
programadores' pasaría a ser 'todes somes programadores'. 

"""

frase = 'todos somos programadores'
palabras = frase.split(' ')
frase_t = ''

for palabra in palabras:
    if palabra[-1] == 'o':
        palabra = palabra[:-1] + palabra[-2].replace('o', 'e')  
    elif palabra[-2] == 'o':
        palabra = palabra[:-2] + palabra[-2].replace('o', 'e') + palabra[-1]      
    frase_t += palabra + " "
print(frase_t.strip())
