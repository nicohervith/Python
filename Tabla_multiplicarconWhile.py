
#Tabla de multiplicar

n = int(input("Ingrese la tabla que desea ver: "))

i = 1

a = 10
''' 
(a) es la variable que limita el ciclo
para simplificar puedo poner while i<= 10

'''


while i <= a:
    print( n * i)
    i = i + 1
print("Tabla de multiplicar del ",n)