import datetime

def esBisiesto(ano):
    flag = False
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        flag = True
    return flag

def diasDelMes(mes, ano):
    dias=30
    if mes in [1,3,5,7,8,10,12]:
        dias=31
    if mes==2:
        if esBisiesto(ano):
            dias=29
        else:
            dias=28
    return dias

def leerFecha():    
    flag=True
    while(flag):
        ano = int(input("Introduce el año: "))
        mes = int(input("Introduce el mes: "))
        dia = int(input("Introduce el día: "))
        if dia<0 or mes<0 or mes>12 or (dia>diasDelMes(mes,ano)):
            print("Fecha inválida, inténtelo de nuevo")
        else:
            flag=False    
    fecha = datetime.date(ano, mes, dia)   
    return fecha

def calcularDiaJuliano(fecha):   
    x = fecha.timetuple()
    return x.tm_yday

print("Introduce una fecha para conocer su Día Juliano")
print("El día Juliano de esa fecha es el",calcularDiaJuliano(leerFecha()))

