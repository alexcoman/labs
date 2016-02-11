#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

    STÂNGA 2
    JOS 2
    DREAPTA 5

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.
"""
from __future__ import print_function


def distanta():
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    ccx, ccy = 0, 0
    with open("istoric.tuxy", "r") as fin:
        for mesaj in fin:
            alfa = mesaj.split()
            beta = alfa[0]
            if beta[:2] == 'SU':
                ccx += int(alfa[1])
            if beta[0] == 'D':
                ccy += int(alfa[1])
            if beta[0] == 'J':
                ccx -= int(alfa[1])
            if beta[:2] == 'ST':
                ccy -= int(alfa[1])
    print((ccx * ccx + ccy * ccy) ** 0.5)

if __name__ == "__main__":
    distanta()
