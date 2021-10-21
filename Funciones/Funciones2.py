"""Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""


def calcularMaxMin(lista):
    a=max(lista)
    b=min(lista)
    return a,b
  
lista=[]
flag=True
print("Introduzca una serie de números para obtener su máximo y su mínimo\n---------------------------------------------------------------------------------")
while flag:   
    try:
        lista.append(int(input("Introduzca un número entero. Pulse cualquier otra tecla para terminar: ")))
    except ValueError:
            flag=False

maxMin=calcularMaxMin(lista)

print("---------------------------------------------------------------------------------------------")
print("El máximo de la lista es",maxMin[0],",el mínimo es",maxMin[1])







