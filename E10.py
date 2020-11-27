import os
os.system('cls')
#P7E10
#Escribe un programa que te pida una palabra o número, pase 
# por parámetro estos datos a una función, y ésta te diga si 
# es o no palíndroma o capicúa. El programa principal imprimirá 
# el resultado de la función:

cadena=input("Dime algo: ")

def f (a):
    holder=""
    for i in range(len(a)-1,-1,-1):
        holder+=(a[i])
    if holder==a:
        return "%s es capicúa o palíndroma." %(a)
    
    return "%s no es capicúa o palíndroma." %(a)   

print(f(cadena))

# if holder==cadena:
#        return True
#    else:
#        return False         #este else no hace falta, el return fuera de la identacion hace lo mismo??
#
#capicua=f(cadena)
#if capicua:
#    print("%s es capicúa o palíndroma." %(cadena))
#else:
#    print("%s no es capicúa o palíndroma." %(cadena))

#/////////////////////////////
#w = ""
#for i in x:
#   w = i + w       //El orden de la suma cambia la posicion de los caracteres en la nueva cadena!!!
