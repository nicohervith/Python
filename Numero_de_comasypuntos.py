

frase_usuario = input("Dime una frase: ")

los_puntos = (".")
las_comas = (",")

l_comas = 0

n_puntos = 0

for puntocoma in frase_usuario:
    if puntocoma in los_puntos:
        n_puntos += 1
    else:
        l_comas += 1

print("El número de puntos es {}".format(n_puntos))
print("El número de comas es {}".format(l_comas))
