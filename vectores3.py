
import random

def vector_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(0,10)
    return vector

#CON RANDINT LIMITO LA CANTIDAD DE NUMEROS ALEATORIOS

print("Ingrese la cantidad de números random que quiere: ")
n = int(input())

aleatorio = vector_aleatorio(n)

print(aleatorio)


