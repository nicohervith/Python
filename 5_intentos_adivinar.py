number_to_guess = 8
user_number = int(input("adivina un numero del 1 al 10,tienes 5 oportunidades: "))
if number_to_guess == user_number:
    print("has ganado")
else:
    print("no")
user_number = int(input("volve a intentarlo"))
if number_to_guess == user_number:
    print("has ganado")
else:
    print("no, tampoco")
user_number = int(input("tercera la vencida"))
if number_to_guess == user_number:
    print("has ganado")
else:
    print("dale bobo")
user_number = int(input("cuarto intento"))
if number_to_guess == user_number:
    print("al fin, ganaste")
else:
    print("ultima oportunidad")
user_number = int(input("ni que fuera tan dificil"))
if number_to_guess == user_number:
    print("bien bobo")
else:
    print("jaja, fracasado")