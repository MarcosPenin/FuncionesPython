

def EsMultiplo(num1,num2):
    flag=True
    if num1%num2!=0:
        flag=False
    return flag

num1=int(input("Introduce un número:"))
num2=int(input("Introduce otro número:"))

if(EsMultiplo(num1,num2)):
    print("El primer número es múltiplo del segundo")
else:
    print("El primer número no es múltiplo del segundo")







