#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Parcurge recursiv si afiseaza fisiere cu a in nume."""

from __future__ import print_function
import os


def fnc(cdir, val):
    """Cauta si afiseaza recursiv fisierele ce contin a."""
    for fisier in os.listdir(cdir):
        if os.path.isdir(os.path.join(cdir, fisier)):
            if val.lower() in fisier.lower():
                print (os.path.join(cdir, fisier))
            fnc(os.path.join(cdir, fisier), val)
        else:
            if val.lower() in fisier.lower():
                print (os.path.join(cdir, fisier))


if __name__ == "__main__":
    fnc("/home/random/Desktop/bcopy", 'a')
