#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy  dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

El dorește să adauge o unealtă care să permită umplerea unei
forme închise.

Exemplu:

Pornim de la imaginea inițială reprezentată mai jos, trebuie să
umplem formele în care se află "x":

  |-----*------|          |******------|         |************|
  |--x--*------|          |******------|         |************|
  |******------|  ----->  |******------|  -----> |************|
  |-----******-|          |-----******-|         |-----*******|
  |-----*---*--|          |-----*---*--|         |-----*---***|
  |-----*---*-x|          |-----*---*--|         |-----*---***|

"""
from __future__ import print_function


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    pozx = punct[0]
    pozy = punct[1]
    if imagine[pozx][pozy] != '*':
        imagine[pozx][pozy] = '*'
        if pozx < (len(imagine) - 1):
            umple_forma(imagine, (pozx + 1, pozy))
        if pozx > 0:
            umple_forma(imagine, (pozx - 1, pozy))
        if pozy < (len(imagine[0]) - 1):
            umple_forma(imagine, (pozx, pozy + 1))
        if pozy > 0:
            umple_forma(imagine, (pozx, pozy - 1))
        return imagine


def main():
    """  Main function docstring """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]

    for i in range(0, len(imaginea)):
        print("".join(imaginea[i]))
    print()
    umple_forma(imaginea, (1, 3))
    for i in range(0, len(imaginea)):
        print("".join(imaginea[i]))
    print()
    umple_forma(imaginea, (5, 11))
    for i in range(0, len(imaginea)):
        print("".join(imaginea[i]))


if __name__ == "__main__":
    main()
