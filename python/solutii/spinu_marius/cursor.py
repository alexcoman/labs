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
from math import hypot


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.
    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """

    _ox = 0

    _oy = 0

    command = []

    try:
        istoric_file = open("istoric.tuxy", "r+")
    except IOError:
        print "Error reading file"
        return

    for line in istoric_file.read().splitlines():
        for char in line:
            if char.isdigit():
                command_string = ''.join(command)
                if command_string == "stanga":
                    _ox = _ox - int(char)
                elif command_string == "dreapta":
                    _ox = _ox + int(char)
                elif command_string == "sus":
                    _oy = _oy + int(char)
                elif command_string == "jos":
                    _oy = _oy - int(char)

                command = []

            else:
                if char != ' ':
                    command.append(char)

    print "Pozitie curenta : (" + str(_ox) + "," + str(_oy) + ")\n"
    print "Distanta fata de origine : " + str(hypot(_ox, _oy))

    # am folosit functia hypot din libraria math pentru formula distantei
    # dintre 2 pct A,B

if __name__ == "__main__":
    distanta()
