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


def on_image(imagine, row, column):

    """
    Functia verifica daca punctul, descris de coordonatele sale - row si
    column, este pe imagine. Returneaza True daca se afla pe imagine,
    False - in caz contrar.
    """

    return not ((row < 0) or (row > len(imagine) - 1) or
                (column < 0) or (column > len(imagine[0]) - 1))


def recursive_fill(imagine, row, column):

    """
    Functia primeste imaginea si coordonatele unui punct gol
    (pe matrice, caracterul '-'), il coloreaza (pe matrice, caracterul '*')
    dupa care verifica cele 4 puncte vecine. Daca un punct vecin este gol,
    functia se autoapeleaza cu aceeasi imagine dar punctul fiind vecinul.
    """

    imagine[row][column] = '*'
    if on_image(imagine, row, column - 1) and imagine[row][column - 1] == '-':
        recursive_fill(imagine, row, column - 1)
    if on_image(imagine, row, column + 1) and imagine[row][column + 1] == '-':
        recursive_fill(imagine, row, column + 1)
    if on_image(imagine, row - 1, column) and imagine[row - 1][column] == '-':
        recursive_fill(imagine, row - 1, column)
    if on_image(imagine, row + 1, column) and imagine[row + 1][column] == '-':
        recursive_fill(imagine, row + 1, column)


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """

    if not on_image(imagine, punct[0], punct[1]):
        return "Punctul {} nu se afla pe imagine.".format(punct)

    if imagine[punct[0]][punct[1]] == '-':
        recursive_fill(imagine, punct[0], punct[1])


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
