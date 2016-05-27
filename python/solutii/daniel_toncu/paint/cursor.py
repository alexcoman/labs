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

import os


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """

    try:
        fisier = open(os.path.join("..", "..", "..", "date_intrare",
                                   "istoric.tuxy"), "r")
        istoric = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține istoricul."
        return

    axa_ox = 0
    axa_oy = 0

    for miscare in istoric.splitlines():
        try:
            distance = int(miscare.split(" ")[1])
        except ValueError:
            print "Mișcare Invalidă - \"{}\".".format(miscare)
            return
        sens = miscare.split(" ")[0]
        if sens == 'JOS':
            axa_oy -= distance
        if sens == 'SUS':
            axa_oy += distance
        if sens == 'STÂNGA':
            axa_ox -= distance
        if sens == 'DREAPTA':
            axa_ox += distance

    return (abs(axa_ox) ** 2 + abs(axa_oy) ** 2) ** 0.5


if __name__ == "__main__":
    distanta()
