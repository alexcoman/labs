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


def check_point(imagine, punct):
    """Verifica daca un punct se afla in imagine """
    return (punct[0] >= 0 and punct[0] < len(imagine)) and\
           (punct[1] >= 0 and punct[1] < len(imagine[0]))


def umple_aux(imagine, punct):
    """ Umple un punct daca poate, daca da merge si pe vecini lui,
    daca nu se opreste """
    if check_point(imagine, punct):
        if imagine[punct[0]][punct[1]] == '-':
            imagine[punct[0]][punct[1]] = '*'
            umple_aux(imagine, (punct[0]-1, punct[1]))
            umple_aux(imagine, (punct[0]+1, punct[1]))
            umple_aux(imagine, (punct[0], punct[1]-1))
            umple_aux(imagine, (punct[0], punct[1]+1))


def afisare(imagine):
    """Afiseaza o imagine """
    for line in imagine:
        for element in line:
            print(element, end="")
        print()
    print()


def umple(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.
    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    umple_aux(imagine, punct)
    afisare(imagine)


def main():
    """ main function """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple(imaginea, (1, 3))
    umple(imaginea, (5, 11))


if __name__ == "__main__":
    main()
