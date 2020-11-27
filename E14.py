import os
os.system('cls')
#P7E14
#Aprovechando el potencial de los diccionarios, escribe un programa
#  que llame a un procedimiento, que recibe como parámetro la fecha
#  en números y devuelve la fecha  con el nombre del mes. Comentario:
#  no es necesario validar si la es correcta, damos por hecho que lo será. 

d = {"01": "Enero", "02" : "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio",
"08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}

fecha=input("Introduce una fecha en formato dd/mm/aaaa: ")

def fechaFormato(a,b):
    dia=a[0:2]
    mes=a[3:5]
    año=a[-4:]
    mesFormato = b.get(mes)
    print("%s de %s de %s" %(dia, mesFormato, año))

fechaFormato(fecha,d)



#def nombre_mes(fecha):
#
#    dia,mes,año=fecha[:2],fecha[3:5],fecha[-4:]
#    meses={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
#    for k,v in meses.items():
#        if mes==k:
#            mes1=meses.get(k)
#    print(dia,"de",mes1,"de",año)
