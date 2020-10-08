# GENERAR LOS MÚLTIPLOS DE 3
# M = INTERRUPTOR

n = int(input("Ingrese un número: "))
m = 3

for i in range(1, n+1):
    print(m, end=', ')
    m = m+3