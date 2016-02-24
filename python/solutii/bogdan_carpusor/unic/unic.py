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
    """Parcurgere cu alocare de memorie suplimentara
    count = {};
    for element in istoric:
        count[element] = count.setdefault(element, 0) + 1

    for key in count:
        if count[key] % 2 > 0:
            return key
    """

    """Parcurgere fara alocare de memorie  """
    result = istoric[0]
    for index in range(1, len(istoric)):
        result = result ^ istoric[index]
    return result

if __name__ == "__main__":
    assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic([1, 1, 1, 2, 2]) == 1
