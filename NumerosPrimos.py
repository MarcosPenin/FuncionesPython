print("NÚMEROS PRIMOS")

num=int(input("Introduce un número para saber si es primo:"))

if num<=1:
    print("El número no es primo")
else:
    cont=2
    cont2=1
    while cont<(num*num):
        if num%cont==0:
            cont2+=1
        cont+=1
    if cont2>2:
        print("El número no es primo")
    else:
        print("El número es primo")





"""" Escribe un programa que diga si un número introducido por teclado
es o no primo. Un número primo es aquel que sólo es divisible entre
él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada
del número para ver si es divisible por algún otro número."""