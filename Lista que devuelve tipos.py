

lista_datos = [1, "asd", 2, 2.1, False, 3, [], 25]

lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)
