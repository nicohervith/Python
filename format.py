

valores_sustituir = [1, 2, "hola", "adios"]
string_a_sustituir = "hola, numero {}, numero {}, {} y {}"

for valor in valores_sustituir:
    string_a_sustituir = string_a_sustituir.replace("{}", str(valor), 1)

print(string_a_sustituir)