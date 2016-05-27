#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema tree."""

from __future__ import print_function
import os
import os.path


def tree(director, nivel):
    """Tree"""
    linii = "-"
    linii = linii * nivel
    lista = os.listdir(director)
    print(linii + director)
    for fis in lista:
        fpath = os.path.join(director, fis)
        if os.path.isfile(fpath):
            print(linii + fis)
        elif os.path.isdir(fpath):
            tree(fpath, nivel + 1)


def main():
    """Main"""
    director = raw_input()
    tree(director, 0)

if __name__ == "__main__":
    main()
