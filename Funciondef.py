# SEPARAR LISTA IMPARES Y PARES

ejemplo = [2,8,4,32,12,9,3]

def separar_listas(lista):
    lista.sort()
    pares = []
    impares = []

    for i in lista:
        if i %2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    return (pares,impares)
pares,impares = separar_listas(ejemplo)

print(pares)
print(impares)