

N = int(input("Ingrese su nota: "))
if N <= 50:
    R = "Reprobado"
elif N >= 70:
    R = "Aprobado"
elif N >= 90:
    R = "Sobresaliente"
else:
    R = "Excelente"

print("Su nota es",N,R)


