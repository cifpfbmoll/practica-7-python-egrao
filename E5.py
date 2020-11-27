import os
os.system('cls')
#P7E5
#Escribe un programa que te pida una frase y una vocal (entrada por teclado),
#  y pase estos datos como parámetro a una función que se encargará de cambiar
#  todas las vocales de la frase por la vocal seleccionada. Devolverá la función
#  la frase modificada, y el programa principal la imprimirá:
frase=input("Dime algo: ")
vocal=input("Dime una vocal: ")
#dictvocal={"a": vocal, "e": vocal, "i": vocal, "o": vocal, "u": vocal}
def f(a,b):
    frase=a.replace("a",b).replace("e",b).replace("i",b).replace("o",b).replace("u",b)
    return frase
print(f(frase,vocal))
