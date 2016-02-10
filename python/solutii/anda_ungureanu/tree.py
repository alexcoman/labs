#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Programul afiseaza indentat continutul folderului
al carui path este dat ca argument.
"""
from __future__ import print_function
import os
import sys


def tree(path, numar):
    """
    Functia afiseaza numele fiecarui fisier din
    path-ul dat, daca este un folder, atunci se
    apeleaza recursiv functia.
    """
    for item in os.listdir(path):
        path_item = os.path.join(path, item)
        print("\t" * numar + "-" + item)
        if os.path.isdir(path_item):
            tree(path_item, numar+1)


if __name__ == "__main__":
    tree(sys.argv[1], 0)
