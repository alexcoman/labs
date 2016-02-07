#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Scrieți o funcție ce să determine maximul dintre două
numere primite ca argument.

Cerințe:
    - Se va folosi structura condițională if-elif-else
    - Nu se va folosi funcția max
"""


def maxim(numar1, numar2):
    """Funcție ce determină maximul dintre două numere."""
    if numar1 > numar2:
        return numar1

    elif numar2 > numar1:
        return numar2

    else:
        # Numerele sunt egale
        return numar1

if __name__ == "__main__":
    assert maxim(1, 2) == 2
    assert maxim(5, 6) == 6
    assert maxim(1, 1) == 1
