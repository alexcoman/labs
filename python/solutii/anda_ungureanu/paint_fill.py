#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy doreste sa implementeze un nou paint pentru consola.
In timpul dezvoltarii proiectului s-a izbit de o problema
pe care nu o poate rezolva singur si a apelat la ajutorul tau.

El doreste sa adauge o unealta care sa permita umplerea unei
forme inchise.

Exemplu:

Pornim de la imaginea initiala reprezentata mai jos, trebuie sa
umplem formele in care se afla x:

  |-----*------|          |******------|         |************|
  |--x--*------|          |******------|         |************|
  |******------|  ----->  |******------|  -----> |************|
  |-----******-|          |-----******-|         |-----*******|
  |-----*---*--|          |-----*---*--|         |-----*---***|
  |-----*---*-x|          |-----*---*--|         |-----*---***|

"""
from __future__ import print_function


def umple(imagine, punct):
    """
    Functia primeste reprezentarea imaginii si coordonatele unui
    punct.
    In cazul in care punctul se afla într-o forma inchisa trebuie sa
    umple forma respectiva cu caracterul "*"
    """
    (x_i, y_i) = punct
    if x_i >= 0 and y_i >= 0 and x_i < len(imagine) and y_i < len(imagine[0]):
        if not imagine[x_i][y_i] is "*":
            imagine[x_i][y_i] = "*"
            umple(imagine, (x_i+1, y_i))
            umple(imagine, (x_i-1, y_i))
            umple(imagine, (x_i, y_i+1))
            umple(imagine, (x_i, y_i-1))


def main():
    """In main se introduce imaginea, se coloreaza si se afiseaza."""
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    for linie in imaginea:
        print(''.join(linie))
    print('\n')
    umple(imaginea, (1, 3))
    umple(imaginea, (5, 11))
    for linie in imaginea:
        print(''.join(linie))


if __name__ == "__main__":
    main()
