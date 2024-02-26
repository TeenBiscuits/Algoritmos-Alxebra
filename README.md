<!--
SPDX-FileCopyrightText: 2024 Pablo Portas López

SPDX-License-Identifier: MIT
-->

# Algoritmos Álxebra

Algoritmos, teoremas, cosas de la asignatura de Álxebra de primero de GEI / UDC en general.

- [Algoritmo de Euclides](src/Algoritmo-de-Euclides.py)
- [Algoritmo de la división entera](src/Algoritmo-de-la-división-entera.py)
- [Criba de Eratóstenes](src/Criba-de-Eratóstenes.py)
- [Máximo común divisor](src/Máximo-común-divisor.py)
- [Teorema de Bezout](src/Teorema-de-Bezout.py)

## Teorema fundamental de la Aritmética

> Para cada |n| >= 2 existen números primos p_1, p_2, ..., p_r tales que
>
> n = +- p_1 * p_2 * ... p_r con p_1 <= p_2 <= ... <= p_r.
>
> Además, esta factorización es única

```python
mcm(a,b) = abs(a*b) / mcd(a,b)
```