#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Afisare arborescenta a structurii unui director."""

from __future__ import print_function
import os


def fnc(cdir, level):
    """Afiseaza recursiv structura arborescenta a unui director."""
    print ('|___' * level, os.path.basename(cdir))
    for fisier in os.listdir(cdir):
        if os.path.isdir(os.path.join(cdir, fisier)):
            fnc(os.path.join(cdir, fisier), level+1)
        else:
            print ('|___' * (level+1), os.path.basename(fisier))


if __name__ == "__main__":
    fnc("/home/random/Desktop/acum", 0)
