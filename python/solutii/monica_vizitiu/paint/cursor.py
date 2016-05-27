#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy  dorește să împlementeze un nou paint pentru consolă.

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

import math

def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    lin = 0
    col = 0
    try:
        fisier = open("istoric.tuxy", "r")
        istoric = fisier.read()
        fisier.close()
    except IOError:
        print("Eroare la citirea din fisier.")
        return
    for miscare in istoric.splitlines():
        curent = miscare.split(' ')
        if curent[0] == "SUS":
            lin -= int(curent[1])
        elif curent[0] == "JOS":
            lin += int(curent[1])
        elif curent[0] == "STANGA":
            col -= int(curent[1])
        else:
            col += int(curent[1])
    print(math.hypot(lin, col))


if __name__ == "__main__":
    distanta()
