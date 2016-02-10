#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
    Programul afiseaza toate fisierele din path-ul
dat care contin litera 'a' in nume.
"""
from __future__ import print_function
import os
import sys


def parcurgere(fila):
    """
    Pentru fiecare fisier, se verifica daca numele
    contine litera 'a', in caz afirmativ, se afiseaza numele,
    altfel, daca este director se apeleaza recursiv functia,
    daca este fisier se trece la urmatorul fisier.
    """
    for item in os.listdir(fila):
        item = os.path.join(fila, item)
        if os.path.isfile(item) and ('a' in item):
            print(item)
        if os.path.isdir(item):
            parcurgere(item)


if __name__ == "__main__":
    parcurgere(sys.argv[1])
