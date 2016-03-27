#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

El dorește să adauge o unealtă care să permită umple_formarea unei
forme închise.

Exemplu:

Pornim de la imaginea inițială reprezentată mai jos, trebuie să
umple_formam formele în care se află "x":

  |-----*------|          |******------|         |************|
  |--x--*------|          |******------|         |************|
  |******------|  ----->  |******------|  -----> |************|
  |-----******-|          |-----******-|         |-----*******|
  |-----*---*--|          |-----*---*--|         |-----*---***|
  |-----*---*-x|          |-----*---*--|         |-----*---***|

"""


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple_forma forma respectivă cu caracterul "*"
    """
    pozitia_pctx, pozitia_pcty = punct[0], punct[1]
    if imagine[pozitia_pctx][pozitia_pcty] == '*':
        return
    imagine[pozitia_pctx][pozitia_pcty] = '*'
    if pozitia_pcty < (len(imagine[0]) - 1):
        umple_forma(imagine, (pozitia_pctx, pozitia_pcty + 1))
    if pozitia_pcty >= 1:
        umple_forma(imagine, (pozitia_pctx, pozitia_pcty - 1))
    if pozitia_pctx < (len(imagine) - 1):
        umple_forma(imagine, (pozitia_pctx + 1, pozitia_pcty))
    if pozitia_pctx >= 1:
        umple_forma(imagine, (pozitia_pctx - 1, pozitia_pcty))
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
    umple_forma(imaginea, (1, 3))
    umple_forma(imaginea, (5, 11))
    for i in range(0, len(imaginea)):
        for j in range(0, len(imaginea[0])):
            print(imaginea[i][j], " ")


if __name__ == "__main__":
    main()
