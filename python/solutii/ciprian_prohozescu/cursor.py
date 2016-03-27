"""Docstring."""
from __future__ import print_function
import math


def distanta():
    """Docstring.calculate_distance"""
    orizontala = 0
    verticala = 0
    intrare = open("istoric.tuxy", "r")
    istoric = intrare.read()
    print (istoric)
    for linie in istoric.splitlines():
        for cuvant in linie.split(' '):
            if cuvant[0] == 'S':
                if cuvant[1] == 'U':
                    directie = 1
                else:
                    directie = 4
            elif cuvant[0] == 'D':
                directie = 2
            elif cuvant[0] == 'J':
                directie = 3
            else:
                adauga = int(cuvant)
                if directie == 1:
                    verticala -= adauga
                elif directie == 2:
                    orizontala += adauga
                elif directie == 3:
                    verticala += adauga
                else:
                    orizontala -= adauga
    dist = math.sqrt(orizontala * orizontala + verticala * verticala)
    print(dist)


if __name__ == "__main__":
    distanta()
