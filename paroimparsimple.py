#Identificar par e impar

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número mayor al primero: "))

if n2 <= n1:
    print("Ingrese un número mayor al primero: ")
for i in range(n1, n2+1):
    if i % 2 == 0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")