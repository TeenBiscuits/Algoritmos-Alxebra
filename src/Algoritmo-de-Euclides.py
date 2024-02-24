# SPDX-FileCopyrightText: 2024 Pablo Portas López
#
# SPDX-License-Identifier: MIT

"""
El llamado Algoritmo de Euclides será usado para calcular mcd(a, b).
Consideramos que a y b son enteros positivos, ya que
mcd(a, b) = mcd(|a|, |b|)
Se efectúa la división del entero mayor a_0 = a entre el menor a_1 = b, obteniéndose como cociente q_1
y como resto a_2.
A continuación se divide a_1 entre a_2, obteniéndose como cociente q_2 y resto a_3. Se continúa hasta
obtener una división exacta, es decir un a_(k+1) = 0.
Tenemos que
a_0 = a >= b = a_1 > a_2 > a_3 > ... > a_k > 0.
Los restos son números enteros positivos, por eso se llegará a un resto nuo a_(k+1) = 0 y a_k != 0.
"""

print("Algoritmo de Euclides")
a = int(input("Introduzca el primer entero (mayor): "))
b = int(input("Introduzca el segundo entero (menor): "))


def euclides(a, b):
    # Arrays de restos, con los enteros en valor absoluto
    euc = [abs(a),abs(b)]
    # El índice en posición 1
    indice = 1
    while euc[indice] != 0:
        # El siguiente elemento será el resto de la división de los dos anteriores
        euc.append(euc[indice - 1] % euc[indice])
        # El índice se mueve a la posición siguiente
        indice += 1
    # Finalmente, la última posición del array es 0, la anterior es el mcd
    return euc[indice - 1]


# Se prueba la función
mcd = euclides(a, b)
print("El máximo común divisor de", a, "y", b, "es:", mcd)
