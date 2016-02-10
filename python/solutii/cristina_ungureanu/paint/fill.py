#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Coloreaza o imagine-lista."""

from __future__ import print_function


def umple(imagine, punct):
    """Umple recursiv imaginea cu * in functie de start."""
    if (punct[0] >= 0 and
            punct[1] >= 0 and
            punct[0] < len(imagine) and
            punct[1] < len(imagine[0]) and
            imagine[punct[0]][punct[1]] != "*"):
        imagine[punct[0]][punct[1]] = "*"
        umple(imagine, (punct[0]-1, punct[1]))
        umple(imagine, (punct[0]+1, punct[1]))
        umple(imagine, (punct[0], punct[1]-1))
        umple(imagine, (punct[0], punct[1]+1))


def main():
    """Apeleaza metoda de colorare pentru imagine."""
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
    for iidx, _ in enumerate(imaginea):
        for jidx, _ in enumerate(imaginea[0]):
            print (imaginea[iidx][jidx], end="")
        print (end="\n")


if __name__ == "__main__":
    main()
