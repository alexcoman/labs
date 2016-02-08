#!/usr/bin/env python
"""
Afiseaza structura aborescenta a fisierelor
"""

from __future__ import print_function
import os
import argparse


def parse():
    """ Parseaza argumentele din CLI"""
    args = argparse.ArgumentParser()
    args.add_argument('dirName', type=str, help="De unde afisam")

    args = args.parse_args()
    return args


def tree(path, indent):
    """ Afiseaza structura arborescenta a directoarelor """
    path = os.path.abspath(path)
    for item in os.listdir(path):
        print(indent, item)
        if os.path.isdir(os.path.join(path, item)):
            tree(os.path.join(path, item), indent+"-")


def main():
    """ main """
    args = parse()
    tree(args.dirName, " ")


if __name__ == "__main__":
    main()
