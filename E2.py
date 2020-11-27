import os
os.system('cls')
#P7E2
#Escribe un programa que lea (entrada por teclado) el nombre 
#y los dos apellidos de una persona (en tres cadenas de caracteres diferentes),
# los pase como parámetros a una función, y ésta debe unirlos y devolver una única
# cadena. La cadena final la imprimirá el programa por pantalla.

nombre=input("Introduzca su nombre: ")
apellido1=input("Introduzca su primer apellido: ")
apellido2=input("Introduzca su segundo apellido: ")
def f(nombre, apellido1, apellido2):
    #s=" "
    seq=(nombre, apellido1, apellido2)
    cadenafinal=" ".join(seq)
    return(cadenafinal)
#cadenafinal=f(nombre, apellido1, apellido2)
#print(cadenafinal)
print(f(nombre, apellido1, apellido2).title())
#print(cadenafinal.title())
