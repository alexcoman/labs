#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema from_icao."""
from __future__ import print_function

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(cale):
    """Transformare din icao"""
    try:
        fisier = open(cale, "r")
        mesaj_icao = fisier.read()
        fisier.close()
    except IOError:
        print("Eroare la citirea din fisier.")
        return
    fisier_out = open('icao_intrare', 'w')
    for mesaj in mesaj_icao.splitlines():
        for msg in mesaj.split(' '):
            for tuplu in ICAO.items():
                if tuplu[1] == msg:
                    fisier_out.write(tuplu[0]+',')
                    break
        fisier_out.write('\n')


if __name__ == "__main__":
    din_icao("mesaj.icao")
