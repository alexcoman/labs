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


def umple(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    randuri = len(imagine)
    if randuri:
        coloane = len(imagine[0])
    else:
        print "Imagine goala"
        return
    if not (punct[0] >= 0 and punct[0] <= randuri and
            punct[1] >= 0 and punct[1] <= coloane):
        return
    if imagine[punct[0]][punct[1]] == "*":
        return
    imagine[punct[0]][punct[1]] = "*"
    vecini = [(punct[0] + 1, punct[1]), (punct[0] - 1, punct[1]),
              (punct[0], punct[1] + 1), (punct[0], punct[1] - 1)]
    for vecin in vecini:
        umple(imagine, vecin)


def main():
    """apeleaza functia umple pe imaginea precizata"""
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
