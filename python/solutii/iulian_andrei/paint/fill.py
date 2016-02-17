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


class Point(object):
    """Clasa pentru reprezentarea unui punct"""
    def __init__(self, fst, snd):
        """Constructor"""
        self.fst = fst
        self.snd = snd


class Queue(object):
    """Clasa pentru implementarea cozii"""
    def __init__(self):
        """Contructor"""
        self.items = []

    def is_empty(self):
        """Return truth value for empty queue"""
        return self.items == []

    def in_queue(self, item):
        """Push new item into queue"""
        self.items.insert(0, item)

    def out_queue(self):
        """Pull elemnt out of queue"""
        return self.items.pop()


def umple(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    pct = Point(punct[0], punct[1])
    queue = Queue()
    queue.in_queue(pct)
    while not queue.is_empty():
        cpoint = queue.out_queue()
        if imagine[cpoint.fst][cpoint.snd] == "*":
            continue
        else:
            imagine[cpoint.fst][cpoint.snd] = "*"

            if cpoint.fst - 1 >= 0 and\
               imagine[cpoint.fst - 1][cpoint.snd] != "*":
                queue.in_queue(Point(cpoint.fst - 1, cpoint.snd))

            if cpoint.fst + 1 < len(imagine) and\
               imagine[cpoint.fst + 1][cpoint.snd] != "*":
                queue.in_queue(Point(cpoint.fst + 1, cpoint.snd))

            if cpoint.snd - 1 >= 0 and\
               imagine[cpoint.fst][cpoint.snd - 1] != "*":
                queue.in_queue(Point(cpoint.fst, cpoint.snd - 1))

            if cpoint.snd + 1 < len(imagine[0]) and\
               imagine[cpoint.fst][cpoint.snd + 1] != "*":
                queue.in_queue(Point(cpoint.fst, cpoint.snd + 1))

    print imagine[0]
    print imagine[1]
    print imagine[2]
    print imagine[3]
    print imagine[4]
    print imagine[5]
    print '\n'


def main():
    """Main function"""
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
