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
import traceback


def umple_forma(imaginea, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """

    cond_1 = punct[0] > len(imaginea) or punct[0] < 0
    cond_2 = punct[1] > len(imaginea[1]) or punct[1] < 0

    if not cond_1 and not cond_2:
        if imaginea[punct[0]][punct[1]] == '*':
            return
        imaginea[punct[0]][punct[1]] = '*'
        if punct[0] - 1 >= 0:
            if imaginea[punct[0] - 1][punct[1]] == '-':
                umple_forma(imaginea, (punct[0] - 1, punct[1]))
        if punct[0] + 1 < len(imaginea):
            if imaginea[punct[0] + 1][punct[1]] == '-':
                umple_forma(imaginea, (punct[0] + 1, punct[1]))
        if punct[1] - 1 >= 0:
            if imaginea[punct[0]][punct[1] - 1] == '-':
                umple_forma(imaginea, (punct[0], punct[1] - 1))
        if punct[1] + 1 < len(imaginea[1]):
            if imaginea[punct[0]][punct[1] + 1] == '-':
                umple_forma(imaginea, (punct[0], punct[1] + 1))
    elif len(traceback.format_stack()) < 4:
        print("Punctul dat nu este valid")


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
    umple_forma(imaginea, (5, 11))


if __name__ == "__main__":
    main()
