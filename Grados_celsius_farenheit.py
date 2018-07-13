

user = input("¿Querés transformar grados Celsius a Farenheit? (si/no)")

if user == "si":
    grados_celsius = int(input("introduce la cantidad de grados Celsius que deseas transformar"))
    grados_farenheit = (grados_celsius * 1.8) + 32
    print("{} grados celsius son {} grados farenheit".format(grados_celsius, grados_farenheit))
else:
    print("ok chao :v")

