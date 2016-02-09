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
import cmath


def distanta():
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    cord_x = 0
    cord_y = 0
    fis = open("istoric.tuxy", "r")
    history = fis.read()
    for line in history.splitlines():
        inst = line.split(' ')
        if inst[0] == "STÂNGA":
            cord_x -= int(inst[1])
        if inst[0] == "DREAPTA":
            cord_x += int(inst[1])
        if inst[0] == "SUS":
            cord_y += int(inst[1])
        if inst[0] == "JOS":
            cord_y -= int(inst[1])
    print(cord_x, ' ', cord_y)
    print(cmath.sqrt(cord_x ** 2 + cord_y ** 2))


if __name__ == "__main__":
    distanta()
