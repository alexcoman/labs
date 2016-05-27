#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""

import os

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def traduce(icao_inv, cuvant):

    """
    Functia, daca cuvantul primit ca parametru este nenul,
    returneaza traducerea sa conform dictionarului icao_inv;
    altfel, returneaza cuvantul nul - ""
    """

    if cuvant:
        return icao_inv[cuvant]

    return ""


def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """

    icao_inv = {value: key for key, value in ICAO.items()}

    try:
        fisier = open(os.path.join("..", "..", "..", "date_intrare", mesaj),
                      "r")
        mesaj_brut = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține mesajul brut."
        return

    try:
        fisier = open("icao_intrare", "w")
        fisier.write("\n".join(" ".join(traduce(icao_inv, cuvant)
                                        for cuvant in linie.split(" "))
                               for linie in mesaj_brut.split("\n")))
        fisier.close()
    except IOError:
        print "Nu am putut genera fișierul icao_intrare."
        return


if __name__ == "__main__":
    din_icao("mesaj.icao")
