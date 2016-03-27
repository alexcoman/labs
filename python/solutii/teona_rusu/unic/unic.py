#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""În laboratorul lui Tuxy toți cercetătorii au asignat un id
de utilizator.

Pentru fiecare cercetător se salvează într-o listă de fiecare
dată când a deschis ușa (fie pentru a intra, fie pentru a ieși).

Tuxy suspectează că cineva rămâne tot timpul după program și
ar dori să scrie un script care să îi verifice teoria, dar
nu a reușit pentru că algoritmul său era prea costisitor pentru
sistem.

Cerințe:
    I. Găsește cercetătorul ce stă peste program după o singură
    parcurgere a listei
    II. Găsește cercetătorul ce stă peste program după o singură
    parcurgere a listei și fără a aloca memorie suplimentară.
"""
# pylint: disable=unused-argument


def gaseste_unic(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1

    Propunerile mele:

    # varianta 1

    d = {}
    for i in istoric:
        if d.has_key(i):
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in d:
        if d[i]%2==1:
            return i

    # varianta 2

    x = 0
    for i in istoric:
        x = x ^ i
    return x
    """

    # varianta 3
    rezultat = istoric.pop()
    while istoric:
        rezultat ^= istoric.pop()
    return rezultat

if __name__ == "__main__":
    assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic([1, 1, 1, 2, 2]) == 1
