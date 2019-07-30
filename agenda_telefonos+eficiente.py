
salida = False

agenda = dict()

while not salida:
    accion = input("Qué querés hacer? agregar número [a], consultar número[c], salir [s]")
    if accion == "a":
        print("añade el nombre y el numero")
        nombre = input("nombre: ")
        numero = input("numero: ")
        agenda[nombre] = numero

    elif accion == "c":
        print("consulta numero")
        nombre = input("de quien quieres saber el numero")
        print(agenda[nombre])

    elif accion == "s":
        salida = True
        print("bye")