
confirmacion = False

while not confirmacion:
    edad_usuario = input("¿Cuántos años tenés?")

    respuesta_edad = input("dijiste {}, es correcto? [si / no]".format(edad_usuario))
    if respuesta_edad == "si":
        confirmacion = True
        print("gueno, flama")