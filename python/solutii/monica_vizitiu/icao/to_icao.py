#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema din icao."""

from __future__ import print_function

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(cale):
    """Din icao"""
    try:
        fisier = open(cale, "r")
        mesaj = fisier.read()
        fisier.close()
    except IOError:
        print("Eroare la citirea din fisier.")
        return
    fisier_out = open('mesaj.icao', 'w')
    for msg in mesaj.splitlines():
        for litera in msg.split(','):
            for tuplu in ICAO.items():
                if tuplu[0] == litera:
                    fisier_out.write(tuplu[1]+' ')
                    break
        fisier_out.write('\n')

if __name__ == "__main__":
    icao("icao_intrare")
