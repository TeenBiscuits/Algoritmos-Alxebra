# SPDX-FileCopyrightText: 2024 Pablo Portas López
#
# SPDX-License-Identifier: MIT

"""
(Teorema de Bezout)
• Si mcd(a, b) = d entonces existen enteros r y s tales que d = ar + bs
• d = mcd(a, b) es el menor entero positivo que se expresa de esa forma.

Caso en especial
mcd(a, b) = 1 si, y solo si, 1 = ar + bs

Calculamos utilizando el algoritmo de Euclides:
Donde suponemos que a y b son enteros positivos, ya que:
mcd(a, b) = mcd(|a|, |b|)
"""

print("Teorema de Bezout usando Euclides")
a = int(input("Introduzca el primer entero (mayor): "))
b = int(input("Introduzca el segundo entero (menor): "))
imp = int(input("¿Quieres imprimir los cálculos por pantalla? (Si: 1 No: 0) "))


def bezout(a, b, imp):
    # Arrays de restos, con los enteros en valor absoluto
    euc = [abs(a), abs(b)]
    # Array de cocientes
    coci = ["-"]
    # Array para r y s
    rind = [1, 0]
    sind = [0, 1]
    # El índice en posición 1
    indice = 1
    while euc[indice] != 0:
        # El siguiente elemento será el resto de la división de los dos anteriores
        euc.append(euc[indice - 1] % euc[indice])
        coci.append(int(euc[indice - 1] / euc[indice]))
        # El índice se mueve a la posición siguiente
        indice += 1
    for i in range(1, indice - 1):
        # Se calculan los valores de r y s
        rind.append(rind[i - 1] - (coci[i] * rind[i]))
        sind.append(sind[i - 1] - (coci[i] * sind[i]))
    # Un guion final en la lista de cocientes, r y s
    coci.append("-")
    rind.append("-")
    sind.append("-")

    if imp == 1:
        # Imprimir la tabla antes de devolver los valores
        print("")
        for i in range(0, indice + 1):
            print('{0:2} | {1:10} | {2:5} | {3:5} | {4:5} |'.format(i, euc[i], coci[i], rind[i], sind[i]))
        print("")
    # Devolver los resultados
    return euc[indice - 1], rind[indice - 1], sind[indice - 1]


# Se prueba la función
d, r, s = bezout(a, b, imp)
print("La ecuación diofántica resultante es: ", d, "= (", r, ") *", a, "+ (", s, ") *", b)
