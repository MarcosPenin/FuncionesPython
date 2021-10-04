print("ORDENAR NÚMEROS DE MAYOR A MENOR")

num1=float(input("Introduce el primer número:"))
num2=float(input("Introduce el segundo número:"))
num3=float(input("Introduce el tercer número:"))

numeros=[num1,num2,num3]

numeros.sort(reverse=True)

print("Los números ordenados de mayor a menor serían:",numeros)



