print("FECHA CORRECTA")

from datetime import datetime

ano=(int(input("Introduce el año:")))
mes=(int(input("Introduce el mes:")))
dia=(int(input("Introduce el día:")))

if mes<0 or dia<0:
    print("La fecha no es válida")
if mes>12:
    print("La fecha no es correcta, los años tienen doce meses")
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    if dia>31:
        print("La fecha no es correcta, ese mes no tiene tantos días")
    else:
        print("La fecha es válida")
if mes==4 or mes==6 or mes==9 or mes==11:
    if dia>30:
        print("La fecha no es correcta, ese mes no tiene tantos días")
    else:
        print("La fecha es válida")
if mes==2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        if dia>29:
            print("La fecha no es correcta, ese mes no tiene tantos días")
        else:
            print("La fecha es válida")
    else:
        if dia>28:
            print("La fecha no es correcta, ese mes no tiene tantos días")
        else:
            print("La fecha es válida")




