
print("CÁLCULO LLEGADA CICLISTA")

print("Introduzca el tiempo de salida de la ciudad A (HH,MM,SS)")
horaSalida=int(input("Hora:"))
minutosSalida=int(input("Minuto:"))
segundosSalida=int(input("Segundo:"))

T=int(input("¿Cuántos segundos tardará en llegar a la ciudad B?"))

horaLlegada = horaSalida + T//3600
if(horaLlegada>23):
    horaLlegada-=24
minutosLlegada = minutosSalida + (T%3600)//60 
if(minutosLlegada>59):
    minutosLlegada-=60
    horaLlegada+=1
    if(horaLlegada>23):
        horaLlegada-=24

segundosLlegada = segundosSalida + (T%3600)%60
if(segundosLlegada>60):
    segundosLlegada-=60
    minutosLlegada+=1
    if(minutosLlegada>59):
        minutosLlegada-=60
        horaLlegada+=1
        if(horaLlegada>23):
            horaLlegada-=24

print("El ciclista llegará a las",horaLlegada, "horas", minutosLlegada, "minutos", segundosLlegada,"segundos")
