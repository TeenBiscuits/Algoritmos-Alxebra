"""
(Criba de Eratóstenes) Sea a un número entero mayor que 1. Si, para
todo primo p con p ≤ √a, se tiene que p -/- a, entonces a es primo.
"""

listaprimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]  # Lista de primos

# Petición de un primo para comprobar
a = int(input("Por favor introduzca un número entero mayor que 2: "))


def cribadeeratostenes(posiprim):
    for i in listaprimos:  # Se avanza primo a primo
        if i ** 2 <= posiprim:  # Todos los primos cuyo cuadrado sea menor o igual al número
            if posiprim % i == 0:  # Si es divisible el número no será primo
                return False
        else:  # Finalmente, si ningún número fue divisor el número es primo
            return True


print("¿El número", a, "es primo?", cribadeeratostenes(a))
