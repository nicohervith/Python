

valores_a_sustituir = ( 1, 2, "hola", "adios")

string_a_sustituir = "no me gusta el numero {}, me encanta que me la metan de a {}, solo te digo {} un polvito y {}"

for valor in valores_a_sustituir:
    string_a_sustituir = string_a_sustituir.replace("{}", str(valor), 1)

print(string_a_sustituir)
