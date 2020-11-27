import os
os.system('cls')
#P7E8
#Escribe un programa que pida una frase (entrada por teclado), 
# y pase la frase como parámetro a una función que debe eliminar 
# los espacios en blanco (compactar la frase). El programa principal 
# imprimirá por pantalla el resultado final.

frase=input("Introduzca una frase: ")
espacio=" "
compacto=""
def f(a):
    frasecompacta=a.replace (espacio, compacto) #puedes usar "" dentro del replace, no hace falta poner variables
    return frasecompacta
print(f(frase))

