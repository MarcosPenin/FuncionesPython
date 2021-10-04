print("FACTORIAL")

cont=1
num=int(input("Introduce un número entero para calcular su factorial:"))

if num<0:
    print("No se puede calcular el factorial de un número negativo")
if num==0:
    print("El factorial de 0 es 1")
if num>0:
    factorial=num
    while cont<num:
        factorial=factorial*cont
        cont+=1
    print("El factorial de",num,"es",factorial)

