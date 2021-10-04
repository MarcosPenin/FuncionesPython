print("TABLA DE MULTIPLICAR 1-5")

num=1
cont=1
cont2=1
while cont2<=5:
    print("Tabla del",num)
    while cont<=10:
        print(num,"*",cont,"=",num*cont)
        cont+=1
    cont2+=1
    cont=1
    num=num+1