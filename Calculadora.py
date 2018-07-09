
primer_numero = int(input("introduce el primer número con el que quieres operar"))

operacion = input("introde la operacion que deseas realizar (suma/resta/division/multiplicacion)")

segundo_numero = int(input("introduce el segundo número con el que quieres operar"))

if operacion == "suma":
    print(primer_numero + segundo_numero)
elif operacion == "resta":
    print(primer_numero - segundo_numero)
elif operacion == "multiplicacion":
    print(primer_numero * segundo_numero)
elif operacion == "division":
    print(primer_numero / segundo_numero)



