#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy doreste sa implementeze un nou paint pentru consola.
In timpul dezvoltarii proiectului s-a izbit de o problema
pe care nu o poate rezolva singur si a apelat la ajutorul tau.
Aplicatia tine un istoric al tuturor miscarilor pe care le-a
facut utlizatorul in fisierul istoric.tuxy
Exemplu de istoric.tuxy:
    STANGA 2
    JOS 2
    DREAPTA 5
Fisierul de mai sus ne spune ca utilizatorul a mutat cursorul
2 casute la stanga dupa care 2 casuse in jos iar ultima actiune
a fost sa pozitioneze cursorul cu 5 casute in dreapta fata de
ultima pozitie.
El doreste un utilitar care sa ii spuna care este distanta dintre
punctul de origine (0, 0) si pozitia curenta a cursorului.
"""
from __future__ import print_function


def distanta():
    """
    Functia citeste continutul fisierului istoric.tuxy si
    calculeaza distanta dintre punctul de origine si pozitia
    curenta a cursorului.
    """
    try:
        fisier = open("istoric.tuxy", "r")
        informatii = fisier.read()
        fisier.close()
    except IOError:
        print("Eroare citire informatii.")
        return
    istoric = {}
    for info in informatii.splitlines():
        (mutari, pasi) = info.split()
        istoric[mutari] = istoric.get(mutari, 0) + int(pasi)
    sus = istoric.get('SUS')
    jos = istoric.get('JOS')
    stanga = istoric.get('STANGA')
    dreapta = istoric.get('DREAPTA')
    coord_x = dreapta - stanga
    coord_y = sus - jos
    distanta_calcul = (coord_x**2+coord_y**2)**0.5
    print(distanta_calcul)


if __name__ == "__main__":
    distanta()
