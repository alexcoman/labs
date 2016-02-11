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


def inrange(imagine, punct):
    """Punctul apartine imaginii
    """
    ccx, ccy = punct
    length = len(imagine[0])
    width = len(imagine)
    if ccx < width and ccx > -1 and ccy < length and ccy > -1:
        return 1
    return 0


def umple(img, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    import Queue
    que = Queue.Queue()
    que.put(punct)
    img[punct[0]][punct[1]] = '*'
    while que.qsize():
        point = que.get()
        sus = (point[0] - 1, point[1])
        jos = (point[0] + 1, point[1])
        stanga = (point[0], point[1] - 1)
        dreapta = (point[0], point[1] + 1)
        if inrange(img, sus) and img[sus[0]][sus[1]] == '-':
            que.put(sus)
            img[sus[0]][sus[1]] = '*'
        if inrange(img, jos) and img[jos[0]][jos[1]] == '-':
            que.put(jos)
            img[jos[0]][jos[1]] = '*'
        if inrange(img, stanga) and img[stanga[0]][stanga[1]] == '-':
            que.put(stanga)
            img[stanga[0]][stanga[1]] = '*'
        if inrange(img, dreapta) and img[dreapta[0]][dreapta[1]] == '-':
            que.put(dreapta)
            img[dreapta[0]][dreapta[1]] = '*'
    print(img)


def main():
    """Main definition
    """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple(imaginea, (1, 3))
    umple(imaginea, (1, 10))

if __name__ == "__main__":
    main()
