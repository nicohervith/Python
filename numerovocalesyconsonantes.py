
frase_usuario = input("Dime una frase: ")

vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")

n_vocales = 0
n_consonantes = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("El número de vocales es {}".format(n_vocales))
print("El número de consonantes es {}".format(n_consonantes))

'''
El número de consonantes no está bien ya que cuenta los espacios, comas, puntos, etc..

'''