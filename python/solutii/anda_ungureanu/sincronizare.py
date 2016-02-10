#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Programul sincronizezaza doua path-uri catre astfel
orice fisier adaugat in unul dintre path-uri este
automat copiat in celalalt path.
"""
from __future__ import print_function
import os
import sys
from shutil import copy


def sincronizare_functie(path1, path2):
    """
    Functia de baza din program verifica daca toate fisierele
    din path1 exista si in path2 , in caz ca un fiesier
    lipseste in path2, il va copia din path1 in path2.
    """
    for item in os.listdir(path1):
        item_path1 = os.path.join(path1, item)
        item_path2 = os.path.join(path2, item)
        if item in os.listdir(path2) and os.path.isfile(item_path1):
            pass
        else:
            if os.path.isfile(item_path1):
                print("+item : "+item+"\n")
                copy(item_path1, item_path2)
            if os.path.isdir(item_path1):
                if item not in os.listdir(path2):
                    print("+item : "+item+"\n")
                    os.makedirs(item_path2)
                sincronizare_functie(item_path1, item_path2)


def main():
    """
    In main se verifica ca cele doua path-uri nu duc
    catre exact acelasi fisier.
    """
    while sys.argv[1] is not sys.argv[2]:
        sincronizare_functie(sys.argv[1], sys.argv[2])
        sincronizare_functie(sys.argv[2], sys.argv[1])

if __name__ == "__main__":
    main()
