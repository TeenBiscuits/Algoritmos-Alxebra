# SPDX-FileCopyrightText: 2024 Pablo Portas López
#
# SPDX-License-Identifier: MIT

"""
Sean a, b ∈ Z son no nulos. El número d es el máximo común
divisor de a y b si es un divisor común de a y b tal que d > 0 y, para cualquier
c ∈ Z tal que c|a y c|b, se tiene que c|d.

Se denota por d = mcd(a, b)
"""

listaprimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))


def divisores(n):  # Algoritmo para calcular divisores (aka. la raya)
    listadiv = [1]
    for i in listaprimos:
        if i <= n and not (n == 0):
            while n % i == 0:
                if n % i == 0:
                    n = n / i
                    listadiv.append(i)
        else:
            return listadiv


def mcd(n1, n2):
    listadiv1 = divisores(n1)  # Divisores del primero número
    listadiv2 = divisores(n2)  # Divisores del segundo número

    maximodiv = 1  # Maximo común divisor

    for i in listadiv1:
        for j in listadiv2:
            if i == j: # Si el número es común se añade al máximo común divisor y se pasa al siguiente
                maximodiv = maximodiv * i
                break
    return maximodiv


print(mcd(a, b))
