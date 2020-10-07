
# PARA QUE ME TOME EN CUENTA LA VARIABLE PONGO F EN EL PRINCIPIO

valor = int(input("Cuántos valores vas a introducir? \n"))

if valor < 1:
    print("error")
else:
    primero = int(input("Escriba un número: "))
    for i in range (valor - 1):
        numero = int(input((f"escriba un número más grande que {primero} : ")))
        # PARA QUE ME TOME EN CUENTA LA VARIABLE PONGO F EN EL PRINCIPIO
        if numero <= primero:
            print(f"{numero} no es mayor que {primero}")
        primero = numero
    print("Gracias por su colaboración")