

user = input("¿Querés transformar grados Celsius a Farenheit? (si/no)")

if user == "si":
    grados_celsius = int(input("introduce la cantidad de grados Celsius que deseas transformar"))
    grados_farenheit = (grados_celsius * 1.8) + 32
    print("{} grados celsius son {} grados farenheit".format(grados_celsius, grados_farenheit))

elif user =="no":
    user2 = input("¿Querés transformar grados Farenheit a Celsius? (si/no)")
    if user2 == "si":
        grados_f = int(input("introduce la cantidad de grados Farenheit que deseas transformar"))
        grados_c = (grados_f / 1.8 ) - 32
        print("{} grados farenheit son {} grados celsius".format(grados_f, grados_c))

print("chao")

