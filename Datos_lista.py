"""
Datos de una lista
"""

lista_datos = [ 1, 2, 23, False, 2.1, 25, 3.8, [], "asd", "s"]
lista_tipos = []
for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)

