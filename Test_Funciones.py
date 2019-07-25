
def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Dijiste {}, ¿Estás seguro?  [ si / no ]".format(dato_usuario))
        if seguro == "si":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("¿Cómo te llamás?")
print("Confirmaste que te llamás {}".format(nombre))

numero = input_con_confirmacion("Dime un número")
print("Confirmaste que el numero es {}".format(numero))