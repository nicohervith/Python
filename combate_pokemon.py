
pokemon_elegido = input("¿Contra quién querés luchar? (Squirtle, Charmander, Bulbasaur)")
#opciones por si la respuesta no es squirtle, charmander o bulbasaur
if pokemon_elegido == "charmander":
    pokemon_elegido = True
elif pokemon_elegido == "bulbasaur":
    pokemon_elegido = True
elif pokemon_elegido == "squirtle":
    pokemon_elegido = True
else:
    print("no se que dijiste, pero perdiste")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0
#elif para ahorrar espacios
if pokemon_elegido == "squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque querés usar? ( Chispazo / Voltio )")

    if ataque_elegido == "chispazo":
      vida_enemigo -= 10
    if ataque_elegido == "voltio":
      vida_enemigo -= 12
    #mostramos el resultado del ataque
    print("la vida de {} es {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("la vida de pikachu ahora es {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Ganaste el combate")

if vida_pikachu <=0:
    print("Perdiste el combate :v")


print("el Combate ha terminado")


