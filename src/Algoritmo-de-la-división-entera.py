# SPDX-FileCopyrightText: 2024 Pablo Portas López
#
# SPDX-License-Identifier: MIT

# Algoritmo de la división entera
# Hay dos únicos enteros q y r que cumplen:
#        0 ≤ r < |b| y a = bq + r

# Variables
# a: dividendo b: divisor r: resto q: cociente

# Pedimos la entrada de datos, solo pueden ser enteros
a = int(input("Introduzca el dividendo: "))
b = int(input("Introduzca el divisor: "))


def algoritmodiv(dividendo, divisor):  # Algoritmo en cuestión
    if dividendo > divisor:
        for i in range(1, dividendo):
            if divisor * i > dividendo:
                break
            else:
                cociente = i
    elif dividendo == divisor:
        cociente = 1
    else:
        cociente = 0

    resto = dividendo - divisor * cociente

    return resto, cociente


# Se prueba el algoritmo
r, q = algoritmodiv(int(a), int(b))

if a == int(b * q) + r and 0 <= r < abs(int(b)):  # Si pasa la prueba, correcto
    print("0 ≤", r, "< |", b, "| y", a, "=", b, "*", q, "+", r)
    print("El resultado de la división entera de", a, "entre", b, "es", q, "con resto", r, ".")
    if r == 0:
        print("La división es exacta.")
    else:
        print("La división no es exacta.")

else:  # Si no pues mal
    print("La división falló.")
