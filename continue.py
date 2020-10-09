# CONTINUE

n = int(input("Ingrese un número: "))
for i in range(1, n+1):

    if n % 2 == 0:
        continue #Salta a la siguiente instrucción
        print(i)
    else:
        print(i)