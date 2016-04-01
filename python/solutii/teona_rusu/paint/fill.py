#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

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


def afisare(imagine):
    """Functia afiseaza imaginea
    """
    for linie in imagine:
        for punct in linie:
            print (punct, end="")
        print ()
    print (end="\n\n")


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    coord_x = punct[0]
    coord_y = punct[1]
    if (coord_x < 0 or coord_x >= len(imagine)) or \
       (coord_y < 0 or coord_y >= len(imagine[coord_x])):
        return
    else:
        if imagine[coord_x][coord_y] == '*':
            return
        else:
            imagine[coord_x][coord_y] = '*'
    umple_forma(imagine, (coord_x, coord_y + 1))
    umple_forma(imagine, (coord_x + 1, coord_y))
    umple_forma(imagine, (coord_x, coord_y - 1))
    umple_forma(imagine, (coord_x - 1, coord_y))


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
    umple_forma(imaginea, (1, 3))
    afisare(imaginea)
    umple_forma(imaginea, (5, 11))
    afisare(imaginea)

if __name__ == "__main__":
    main()
