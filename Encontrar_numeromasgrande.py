

numeros_usuarios = []
numero_del_usuario = ""

while len(numeros_usuarios) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("dime un número: ")
    numeros_usuarios.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("número añadido")

numero_grande = numeros_usuarios [0]

for numero in numeros_usuarios:
    if numero > numero_grande:
        numero_grande = numero

print("El número más grande es {}".format(numero_grande))

