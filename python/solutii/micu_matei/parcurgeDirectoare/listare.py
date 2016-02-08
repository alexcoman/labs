#!/usr/bin/env python

"""
Afiseaza toate pathurile subordonate fisirului de intrare care contin litera A
"""
import os
import sys


def list_file(path):
    """ Afiseaza toate directoarele care contin A"""
    path = os.path.abspath(path)
    for item in os.listdir(path):
        current_path = os.path.join(path, item)
        if os.path.isfile(current_path):
            if 'A' in item:
                print current_path
        elif os.path.isdir(current_path):
            list_file(current_path)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        list_file(sys.argv[1])
    print
