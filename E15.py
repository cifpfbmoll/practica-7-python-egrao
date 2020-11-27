import os
os.system('cls')
#P7E15
#Desarrolla un programa utilizando que nos sirva para gestionar
# nuestros contactos (la información a gestionar
# será el teléfono, nombre, apellido1, apellido2 y correo electrónico. El programa
#  tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto
# a partir de la clave, consultar todos los contactos y eliminar contacto. Aprovecha
# lo que has aprendido hasta el momento (diccionarios, funciones, procedimientos…).

agenda={}   #dict
funciones=["Añadir contacto", "Consultar contacto a partir de un nombre", "Consultar todos los contactos", "Eliminar un contacto", "Cerrar agenda"]

def añadirContacto(d):
    nombre=input("Nombre del contacto: ")
    apellido1=input("Primer apellido: ")
    apellido2=input("Segundo apellido: ")
    telefono=int(input("Telefono del contacto: "))
    email=input("Email del contacto: ")
    listaValores=[apellido1+" "+apellido2,telefono,email]
    d[nombre] = listaValores
    return d

def consultarContacto(d):
    consultaNombre=input("Introduzca el nombre del contacto: ")
    default="No existe"
    print(d.get(consultaNombre, default))


def consultarAgenda(d):
#    for k,v in d.items():
#        print("%s %s" %(k,v))
    for i in d.keys():
        datos=""
        lista=d.get(i)
        for j in lista:
            datos+=str(j)+" "
        print(i,datos)

def eliminarContacto(d):
    eliminarNombre=input("Introduzca contacto a eliminar: ")
    print("¿Seguro que desea eliminar el contacto %s?" %(eliminarNombre))
    check=input("Y/N? ")
    if check=="Y" or check=="y":
        d.pop(eliminarNombre)
        print("%s se ha eliminado de la lista de contactos" %(eliminarNombre))
    return d


#def programa(func):
#    print("Bienvenido a su agenda, ¿qué desea hacer?")
#    for i in func:
#        print(i)
#    accion=input("Elija una opción: ")
#    return accion

print("¿Iniciar la agenda?", end="")
inicio=input("¿Y/N? ")
contador=1
while inicio!="N" and inicio!="n":
    if contador==1:
        print("Bienvenido, ¿qué desea hacer?:")
    for i in funciones:
        print(i)
    print("--------------------------------------------")
    accion=input()
    if accion=="Añadir contacto":
        añadirContacto(agenda)
        contador+=1
        print("--------------------------------------------")
    elif accion=="Consultar contacto a partir de un nombre":
        consultarContacto(agenda)
        contador+=1
        print("--------------------------------------------")
    elif accion=="Consultar todos los contactos":
        consultarAgenda(agenda)
        contador+=1
        print("--------------------------------------------")
    elif accion=="Eliminar un contacto":
        eliminarContacto(agenda)
        contador+=1
        print("--------------------------------------------")
    elif accion=="Cerrar agenda":
        inicio="N"
    else:
        contador+=1
        print("!!!!!!")
        print("Error, inténtelo de nuevo.")
        print("--------------------------------------------")

print("Bye no vemos mañana")
