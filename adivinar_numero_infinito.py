adivina_usuario = input("adivina un numero del 1 al 30, da enter para continuar")

numero_a_adivinar = 29

user_number = 0

intentos_realizados = 0

while numero_a_adivinar != user_number:
    intentos_realizados +=1
    user_number = int(input("introduce el número que crees que es, este es tu intento {}".format(intentos_realizados)))

print("Ganaste con un total de {} intentos".format(intentos_realizados))


