

salida = False

agenda = []

while not salida:

    accion = input("¿Qué quieres hacer? Añadir número [a], Consultar número [c], salir [s] ")
    if accion == "a":

        print("Añadí el número")
        nombre = input("nombre: ")
        numero = input("numero: ")
        agenda.append([nombre, numero])

    elif accion == "c":
        print("Vamos a consultar un número")
        nombre = input("Que número quieres saber?")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])



    elif accion == "s":
        salida = True