import os
os.system('cls')
#P7E3
#Escribe un programa que lea (entrada por teclado) una frase,
#y la pase como parámetro a un procedimiento, y éste debe mostrar
#la frase con un carácter en cada línea.

frase=input("Introduzca una frase: ")
def f(frase):
    for i in range(len(frase)):
        print (frase[i])
f(frase)
