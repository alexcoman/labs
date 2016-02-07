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


def distanta():
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    coord_x = 0
    coord_y = 0
    istoric = open("istoric.tuxy", "r")
    instructions = istoric.read()
    for instruction in instructions.splitlines():
        components = instruction.split()
        try:
            value = int(components[1])
        except ValueError:
            print "Valoare invalida"
            return
        direction = components[0].upper()

        if direction == "STANGA":
            coord_x -= value
        elif direction == "SUS":
            coord_y += value
        elif direction == "DREAPTA":
            coord_x += value
        elif direction == "JOS":
            coord_y -= value
        else:
            print "Directie invalida"
            return
    import math
    print math.sqrt(coord_x*coord_x+coord_y*coord_y)


if __name__ == "__main__":
    distanta()
