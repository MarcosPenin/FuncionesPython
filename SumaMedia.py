print("SUMA Y MEDIA")

print("Introduce números para obtener su suma y su media (introduce un 0 para finalizar")

num=1
suma=0
cont=0
media=0

while(num!=0):
    num=float(input("Introduce un número:"))
    suma=suma+num
    cont=cont+1

media=suma/(cont-1)

print("La suma de los números introducidos es de",suma,"la media es de",media)


