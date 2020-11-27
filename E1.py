import os
os.system('cls')
#P7E1
#Escribe un programa que pida un texto por pantalla, este
#texto lo pase como parámetro a un procedimiento, y éste lo
#imprima primero todo en minúsculas y luego todo en mayúsculas.

texto=input("Introduce un texto: ")
def f(texto):
    print(texto.lower())
    print(texto.upper())
f(texto)
