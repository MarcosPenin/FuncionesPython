
print("CÁLCULO LLEGADA CICLISTA")

print("Introduzca el tiempo de salida de la ciudad A (HH,MM,SS)")
horaSalida=int(input("Hora:"))
minutosSalida=int(input("Minuto:"))
segundosSalida=int(input("Segundo:"))

T=int(input("¿Cuántos segundos tardará en llegar a la ciudad B?"))

horaLlegada = horaSalida + T//3600
minutosLlegada = minutosSalida + (T%3600)//60 
segundosLlegada = segundosSalida + (T%3600)%60

print("El ciclista llegará a las",horaLlegada, "horas", minutosLlegada, "minutos", segundosLlegada,"segundos")
