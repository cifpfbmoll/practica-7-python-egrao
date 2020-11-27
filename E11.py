import os
os.system('cls')
#P7E11
#Escribe un programa que te pida una frase, y pase la frase
# como parámetro a una función. Ésta debe devolver si es palíndroma
# o no, y el programa principal escribirá el resultado por pantalla:

frase=input("Dime algo: ")

def f(a):
    espacio=" "
    compacto=""
    holder=""
    frasecompacta=a.replace (espacio, compacto)
    for i in frasecompacta:
        holder=i+holder
    if frasecompacta==holder:
        return "%s es palíndroma." %(a)
    return "%s no es palíndroma." %(a)

print(f(frase))

