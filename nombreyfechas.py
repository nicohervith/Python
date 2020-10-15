

salida = False

agenda = dict()
while not salida:
    accion = input("Que querés hacer? Agregar fecha [A] / Consultar fecha [C] / Salir [S]")
    if accion == "A":
        nombre = input("Nombre: ")
        fechanacimiento = input("Fecha de nacimiento: ")
        agenda[nombre] = fechanacimiento
    elif accion == "C":
        nombre = input("De quién querés saber la fecha? ")
        print(agenda[nombre])
    else:
        print("chao")

