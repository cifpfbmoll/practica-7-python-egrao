import os
os.system('cls')
#P7E7
#Escribe un programa que lea una frase (entrada por teclado), y la pase 
# como parámetro a un procedimiento. El procedimiento contará el número
# de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

frase=input("Introduce una frase: ")
vocales=["a","e","i","o","u"]
def f(a):
    #count=a.count("a")
    #print(count)
    for i in vocales:
        count=a.count(i)
        if count==1:
            print("La vocal %s aparece %s vez." %(i,count))
        else:
            print("La vocal %s aparece %s veces." %(i,count))
f(frase)
