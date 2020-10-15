
salida = False
colores = {"rojo" : "red", "azul" : "blue" , "amarillo" : "yellow" , "marron" : "brown" , "negro" : "black" ,
           "blanco" : "white", "rosa" : "pink" , "naranja" : "orange" , "violeta" : "purple" , "verde" : "green" }

while not salida:
    accion = input("Que color querés hacer? Ver  colores en inglés [A] / salir [S] ")
    if accion == "A":
        quecolor = input("Qué color querés saber? ")
        print(colores[quecolor])
    else:
        print("chau")

