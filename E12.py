import os
os.system('cls')
#P7E12
#Escribir un programa que lea una frase, y pase ésta como
# parámetro a una función que debe contar el número de
# palabras que contiene. Debe imprimir el programa principal
# el resultado. Asumir que cada palabra está separada por un solo blanco:
#Asumir que cada palabra está separada por un solo blanco.
#No se sabe cómo están separadas las palabras. Pueden estar
#separadas por más de un blanco o por signos de puntuación.

frase=input("Dime algo: ")

def f(a):
    lista=a.split()
    contador=len(lista)
    return contador

print("%s contiene %d palabras" %(frase, f(frase)))
