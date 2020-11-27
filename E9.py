import os
os.system('cls')
#P7E9
#Escribe un programa que pida dos palabras las pase como
# parámetro a un procedimiento y diga si riman o no. Si coinciden
# las tres últimas letras tiene que decir que riman. Si coinciden
# solo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1=input("Dime una palabra: ")
palabra2=input("Dime otra palabra: ")

def f(a,b):
    if (a[-3])==(b[-3]):
        print("Las palabras %s y %s riman." %(palabra1,palabra2))
    elif (a[-2])==(b[-2]):
        print("Las palabras %s y %s riman un poco." %(palabra1,palabra2))
    else:
        print("Las palabras %s y %s no riman." %(palabra1,palabra2))

f(palabra1,palabra2)
