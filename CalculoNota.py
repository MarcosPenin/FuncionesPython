print("CÁLCULO DE LA NOTA DEL ALUMNO")

parcial1=float(input("Introduce la nota del primer parcial:"))
parcial2=float(input("Introduce la nota del segundo parcial:"))
parcial3=float(input("Introduce la nota del tercer parcial:"))
final=float(input("Introduce la nota del examen final:"))
trabajo=float(input("Introduce la nota del trabajo final:"))

nota=(((parcial1+parcial2+parcial3)/3)*0.55)+(final*0.30)+(trabajo*0.15)

print("La nota del alumno es", round(nota,2))

