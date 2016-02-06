#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""În laboratorul lui Tuxy toti cercetătorii au asignat un id
de utilizator.
Pentru fiecare cercetător se salvează într-o listă de fiecare
dată când a deschis usa (fie pentru a intra, fie pentru a iesi).
Tuxy suspectează că cineva rămâne tot timpul după program si
ar dori să scrie un script care să îi verifice teoria, dar
nu a reusit pentru că algoritmul său era prea costisitor pentru
sistem.
Cerinte:
    I. Găseste cercetătorul ce stă peste program după o singură
    parcurgere a listei
    II. Găseste cercetătorul ce stă peste program după o singură
    parcurgere a listei si fără a aloca memorie suplimentară.
"""


def gaseste(istoric):
    """
    Functia primeste o listă cu elemente numerice si trebuie
    să returneze elementul care nu este duplicat.
    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """
    result = 0
    for i in istoric:
        result ^= i
    return result


if __name__ == "__main__":
    assert gaseste([1, 2, 3, 2, 1]) == 3
    assert gaseste([1, 1, 1, 2, 2]) == 1
