
#Serie ABABABABABA....

n = int(input("Ingrese un número: "))

w = 0

for i in range(1,n+1):
    if w == 0:
        print('A')
        w = 1
#EN LA LÍNEA 11 LE DOY A W EL VALOR DE 1 PARA QUE NO SE VUELVA A CUMPLIR EL CICLO DEL IF Y PASE POR ELSE, DE IGUAL MANERA EN ELSE LE DOY EL VALOR DE 0
    else:
        print('B')
        w = 0