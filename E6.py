import os
os.system('cls')
#P7E6
#Escribe un programa que lea el nombre de una persona y un carácter
#(entrada por teclado), le pase estos datos a una función que comprobará
#si dicho carácter está en su nombre. El resultado de dicha función lo 
# imprimirá el programa principal por pantalla.
nombre=input("Introduzca un nombre: ")
caracter=input("Introduzca un caracter: ")
def f(a, b):
    comprobar=a.find(b)
    if comprobar==-1:
        print("El nombre %s no contiene el caracter %s." %(a,b))
    else:
        print("El nombre %s contiene el caracter %s." %(a,b))
    return comprobar
f(nombre, caracter)
