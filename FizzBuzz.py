"""""
Dada una lista de enteros:
Sustituir múltiplos de 3 por un Fizz
y múltiplos de 5 por un Buzz
Múltiplos de 3 y 5 por un FizzBuzz
"""

numeros = [ 1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"

print(numeros)