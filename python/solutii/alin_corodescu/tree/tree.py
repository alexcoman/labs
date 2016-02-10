#!/usr/bin/env python
# *-* coding: UTF-8 *-*

""" Utilitar ce imita "tree" """

import os
import sys


def tree(path, tabs):
    """afiseaza folderul ca structura tree"""
    print "--" * tabs, path.split("/")[-1]
    for name in os.listdir(path):
        pathabs = os.path.join(path, name)
        if os.path.isfile(pathabs):
            print "--" * (tabs+1), name
        if os.path.isdir(pathabs):
            tree(pathabs, tabs+1)

if __name__ == "__main__":
    tree(sys.argv[1], 0)
