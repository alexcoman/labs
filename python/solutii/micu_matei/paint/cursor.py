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
import sys
import os


def is_valid(line):
    """verificam daca linia este valida"""
    line = line.split()
    if len(line) < 1:
        return False

    if line[0] not in ["STANGA", "DREAPTA", "SUS", "JOS"]:
        return False

    try:
        int(line[1])
        return True
    except ValueError:
        return False
    return True


def parse_line(line):
    """Functia primeste o linie si returneaza
    directia ca in care a mers cursorul sub forma unui
    tuple (x, y) """

    if is_valid(line):
        line = line.split()
        move = line[0]
        direction = int(line[1])
        if move == "STÂNGA":
            return (-direction, 0)
        elif move == "DREAPTA":
            return (direction, 0)
        elif move == "JOS":
            return (0, -direction)
        elif move == "SUS":
            return (0, direction)
        return (0, 0)
    else:
        return (0, 0)


def distanta(path):
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    fisier = open(path, 'r')
    data = fisier.read()
    fisier.close()
    pozition = [0, 0]
    for line in data.splitlines():
        point = parse_line(line)
        pozition[0] += point[0]
        pozition[1] += point[1]

    print((pozition[0] ** 2 + pozition[1] ** 2) ** 0.5)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        PATH = sys.argv[1]
        PATH = os.path.abspath(PATH)
        if os.path.exists(PATH) and os.path.isfile(PATH):
            distanta(PATH)
        else:
            print(PATH, " nu este un fisier sau nu exista")
    else:
        print(" nu stim unde este fisierul ")
